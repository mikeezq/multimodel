import os

from flask import Flask, render_template, request, redirect, url_for, session
from config import SQLALCHEMY_DATABASE_URI, basedir
from app.util import signin, signup
from app.models import db

app = Flask(__name__, template_folder=os.path.join(basedir, "templates"), static_folder=os.path.join(basedir, "static"))
print(os.path.join(basedir, "app/static"))

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random_key"
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == "signin":
            ans, status_code = signin(request.form)
            if status_code == 200:
                session['login'] = True
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
    return redirect(url_for('login'))


@app.route('/main', methods=['GET'])
def main():
    if session.get('login', False):
        print("user authorized")
    else:
        return "login please"


    movies = [
        {'title': 'one+one', 'filename': 'one+one.jpg', 'description': 'Классный фильм'},
        {'title': 'countdown', 'filename': 'countdown.jpg', 'description': 'Описание фильма 2'},
        # ...другие фильмы...
    ]


    return render_template('main.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
