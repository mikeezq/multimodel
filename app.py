from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# TODO: Pass from env variables
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://local-db:local-db@localhost:5432/local-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            # You can return a better error page here
            return "Username and password are required.", 400
        user = Users.query.filter_by(username=username).first()
        if user and user.password == password:
            return "Logged in successfully!"
        else:
            return "Failed to login!"
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
