import os

from flask import Flask, render_template, request, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI, basedir
from app.util import signin, signup
from app.models import db

app = Flask(__name__, template_folder=os.path.join(basedir, "templates"), static_folder=os.path.join(basedir, "static"))
print(os.path.join(basedir, "app/static"))

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
                return redirect(url_for('about'))
            return ans, status_code
        elif action == "signup":
            return signup(request.form)
        else:
            return "Password will be reset"

    return render_template('login.html')


@app.route('/main', methods=['GET'])
def about():
    movies = [
        {'title': 'one+one', 'filename': 'one+one.jpg', 'description': 'Классный фильм'},
        {'title': 'countdown', 'filename': 'countdown.jpg', 'description': 'Описание фильма 2'},
        # ...другие фильмы...
    ]

    return render_template('main.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
