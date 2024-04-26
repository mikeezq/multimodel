import os

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_caching import Cache
from flask_admin import expose, AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView

from config import SQLALCHEMY_DATABASE_URI, basedir

from app import db
from app.utils.login_page import signin, signup
from app.models.users import Users
from app.models.movies import Movies
from app.databases import db_repo

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
        Movies
    ]:
        admin.add_view(AuthAdminModelView(table, db.session))


admin = Admin(app, name='Must 2.0 AdminPanel', template_mode='bootstrap3', index_view=AuthAdminIndexView())
activate_admin_views(admin, db)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
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
    session.pop('login')
    session.pop('username')
    return redirect(url_for('login'))


@app.route('/cabinet')
def cabinet():
    login = session.get('login')
    username = session.get('username')
    if not login or not username:
        return redirect(url_for('login'))
    return redirect(url_for('user_cabinet', username=username))


@app.route('/cabinet/<username>')
def user_cabinet(username):
    session_username = session.get('username')
    if username != session_username:
        flash('You do not have permission to view this page.', 'error')
        return redirect(url_for('main'))

    return render_template(
        'cabinet.html',
        username=username,
        user_ratings_count=1,
        user_reviews_count=1,
    )


@app.route('/main', methods=['GET'])
@cache.cached(timeout=50)
def main():
    if not session.get('login', False):
        return redirect(url_for('login'))

    movies = db_repo.get_all_movies()
    data = []
    for movie in movies:
        print(movie.title)
        data.append(
            {'title': movie.title, 'filename': 'countdown.jpg', 'description': 'Классный фильм'},
        )

    return render_template('main.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
