from flask import Flask, render_template, request, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI
from app.util import signin, signup
from app.models import db

app = Flask(__name__)

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
        if action == "signup":
            return signup(request.form)
        elif action == "signin":
            return signin(request.form)
        else:
            return "Password will be reset"

    return render_template('login.html')
