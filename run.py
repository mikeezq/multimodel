import os

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_caching import Cache
from flask_admin import expose, AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView

from config import SQLALCHEMY_DATABASE_URI, basedir

from app import db
from app.utils.login_page import signin, signup
from app.models.users import Users
from app.models.tv_shows import TV_Shows
from app.databases import postgre_repo, mongo_repo

from app.s3.s3 import fill_s3_if_not_filled, get_presigned_url


app = Flask(__name__, template_folder=os.path.join(basedir, "templates"), static_folder=os.path.join(basedir, "static"))
print(os.path.join(basedir, "app/static"))

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random_key"
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)
db.init_app(app)


class AuthAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if 'username' in session and session['username'] == 'admin':
            return super(AuthAdminIndexView, self).index()
        else:
            return redirect(url_for('main'))

    def is_accessible(self):
        return 'username' in session and session['username'] == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main'))


class AuthAdminModelView(ModelView):
    def is_accessible(self):
        return 'username' in session and session['username'] == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main'))


def activate_admin_views(admin, db):
    for table in [
        Users,
        TV_Shows
    ]:
        admin.add_view(AuthAdminModelView(table, db.session))


admin = Admin(app, name='Must 2.0 AdminPanel', template_mode='bootstrap3', index_view=AuthAdminIndexView())
activate_admin_views(admin, db)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    admins, moderators = postgre_repo.get_privileged_users()
    if request.method == 'POST':
        action = request.form.get('action')

        if action == "signin":
            ans, status_code, username = signin(request.form)
            if status_code == 200:
                session['login'] = True
                session['username'] = username
                return redirect(url_for('main'))
            return ans, status_code
        elif action == "signup":
            return signup(request.form)
        else:
            return "Password will be reset"

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    if "login" in session:
        session.pop('login')
    if "username" in session:
        session.pop('username')
    return redirect(url_for('login'))


@app.route('/cabinet')
def cabinet():
    log = session.get('login')
    username = session.get('username')
    if not log or not username:
        return redirect(url_for('login'))
    return redirect(url_for('user_cabinet', username=username))


@app.route('/cabinet/<username>')
def user_cabinet(username):
    session_username = session.get('username')
    if username != session_username:
        flash('You do not have permission to view this page.', 'error')
        return redirect(url_for('main'))

    reviews = postgre_repo.get_user_reviews()

    return render_template(
        'cabinet.html',
        user_avg_reviews_rating=sum(map(lambda x: x.rating, reviews)) / len(reviews),
        user_reviews_count=len(reviews),
        reviews=reviews[:5]
    )


@app.route('/main', methods=['GET'])
@cache.cached(timeout=50)
def main():
    if not session.get('login', False):
        return redirect(url_for('login'))

    shows = postgre_repo.get_all_shows()
    data = []
    for show in shows:
        page_data = {'title': show.title, 'filename': 'countdown.jpg', 'description': 'Классный фильм'}
        mongo_data = {'title': show.title, 'filelink': get_presigned_url("countdown.jpg")}
        data.append(page_data)
        mongo_repo.create_film(mongo_data)

    return render_template('main.html', movies=shows)


if __name__ == "__main__":
    fill_s3_if_not_filled()
    app.run(debug=True)
