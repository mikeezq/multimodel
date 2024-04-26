import os

from flask import Flask, render_template, request, redirect, url_for, session
from flask_caching import Cache
from config import SQLALCHEMY_DATABASE_URI, basedir
from app.utils.login_page import signin, signup
from app import db

app = Flask(__name__, template_folder=os.path.join(basedir, "templates"), static_folder=os.path.join(basedir, "static"))
print(os.path.join(basedir, "app/static"))

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random_key"
app.config['CACHE_TYPE'] = 'simple'  # Вы можете выбрать другой бэкенд, например 'redis', 'memcached'
cache = Cache(app)
db.init_app(app)


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

    movies = [
        {'title': 'one+one', 'filename': 'one+one.jpg', 'description': 'Классный фильм'},
        {'title': 'countdown', 'filename': 'countdown.jpg', 'description': 'Описание фильма 2'},
        # ...другие фильмы...
    ]

    return render_template('main.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
