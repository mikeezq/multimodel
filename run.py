import os

from sqlalchemy import inspect

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_caching import Cache
from flask_admin import expose, AdminIndexView, Admin
from flask_admin.contrib.sqla import ModelView

from config import SQLALCHEMY_DATABASE_URI, basedir

from app import db
from app.utils.login import signin, signup

from app.models.users import Users, Reviews, Wishlists, Watchedlist, Sessions, Payments,\
    Subscriptions, Privileged_Users

from app.models.tv_shows import TV_Shows, Studios, Directors, Actors, TV_ShowActors, TV_ShowDirectors, TV_ShowGenres,\
    Genres, CollectionTV_Shows, Collections, TrailerViews

from app.databases import postgre_repo, mongo_repo
from app.s3.s3 import fill_s3_if_not_filled
from app.utils.main import get_show_reviews
from app.utils.add_new_serial import create_serial_view


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
    column_display_pk = True
    can_view_details = True
    column_hide_backrefs = False

    def is_accessible(self):
        return 'username' in session and session['username'] == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main'))


def activate_admin_views(admin, db):
    for table in [
        Users, TV_Shows, Reviews, Wishlists, Watchedlist, Sessions, Payments, Subscriptions, Privileged_Users,
        Studios, Directors, Actors, TV_ShowActors, TV_ShowGenres, TV_ShowDirectors, CollectionTV_Shows, Genres,
        Collections, TrailerViews
    ]:
        column_list = [c_attr.key for c_attr in inspect(table).mapper.column_attrs]
        ChildView = type(
            f'ChildView{table.__tablename__}',
            (ModelView,),
            {
                'column_display_pk': True,
                'column_hide_backrefs': False,
                'column_list': column_list
            }
        )

        admin.add_view(ChildView(table, db.session))


admin = Admin(app, name='TV serials AdminPanel', template_mode='bootstrap2', index_view=AuthAdminIndexView())
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
                if username in [admin.username for admin in admins]:
                    session['role'] = 'admin'
                elif username in [moderator.username for moderator in moderators]:
                    session['role'] = 'moderator'
                else:
                    session['role'] = 'user'
                return redirect(url_for('main'))
            return render_template('login.html')
        elif action == "signup":
            signup(request.form)
            return render_template('login.html')
        else:
            return "Password will be reset"

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    if "login" in session:
        session.pop('login')
    if "username" in session:
        session.pop('username')
    if "role" in session:
        session.pop('role')
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
        return redirect(url_for('main'))

    reviews = postgre_repo.get_user_reviews(username)

    is_admin = session.get('role') == 'admin'
    return render_template(
        'cabinet.html',
        user_avg_reviews_rating=sum(map(lambda x: x.rating, reviews)) / len(reviews) if len(reviews) else 0,
        user_reviews_count=len(reviews),
        reviews=reviews[:5],
        is_admin=is_admin
    )


@app.route('/add-show', methods=['GET', 'POST'])
def add_show():
    if not session.get('login', False):
        return redirect(url_for('login'))
    if request.method == "POST":
        try:
            create_serial_view(request)
            if session['role'] != 'user':
                flash('Сериал успешно добавлен.', 'success')
        except Exception:
            flash('Не удалось добавить сериал.', 'error')

    shows_data = postgre_repo.get_possible_shows_data()

    is_admin = session.get('role') == 'admin'
    return render_template("add-show.html", shows_data=shows_data, is_admin=is_admin)


@app.route('/main/<title>', methods=['GET'])
def main_show(title):
    if not session.get('login', False):
        return redirect(url_for('login'))

    link = mongo_repo.get_show_link(title)
    show_info = postgre_repo.get_show_info(title)
    show_reviews = get_show_reviews(title)

    is_admin = session.get('role') == 'admin'
    return render_template('show.html', show_info=show_info, link=link, show_reviews=show_reviews, is_admin=is_admin)


@app.route('/main/<title>/submit_review', methods=['POST'])
def submit_review(title):
    comment = request.form.get('review')
    rating = request.form.get('rating', type=float)
    if rating is None or not (0.0 <= rating <= 10.0):
        flash('Рейтинг должен быть числом от 0.0 до 10.0', 'error')
        return redirect(url_for('main_show', title=title))

    username = session.get('username')
    try:
        postgre_repo.add_new_review(title, username, comment, rating)
        flash('Отзыв успешно добавлен.', 'success')
    except Exception as e:
        print(e)
        flash('Ошибка при добавлении отзыва.', 'error')

    return redirect(url_for('main_show', title=title))


@app.route('/main', methods=['GET'])
@cache.cached(timeout=50)
def main():
    if not session.get('login', False):
        return redirect(url_for('login'))

    shows = mongo_repo.get_all_shows()

    is_admin = session.get('role') == 'admin'
    return render_template('main.html', shows=shows, is_admin=is_admin)


if __name__ == "__main__":
    fill_s3_if_not_filled()
    mongo_repo.init_db()
    app.run(debug=True)
