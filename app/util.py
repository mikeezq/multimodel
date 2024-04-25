from app.users.models import Users
from app.models import db


def signin(request_form):
    email = request_form.get('email')
    password = request_form.get('password')
    if not email or not password:
        return "Email and password are required.", 400
    user = Users.query.filter_by(email=email).first()
    if user and user.password == password:
        return "Logged in successfully!", 200
    else:
        return "Failed to login!", 400


def signup(request_form):
    email = request_form.get('email')
    password = request_form.get('password')
    repassword = request_form.get('repassword')
    username = request_form.get('username')

    if not email or not password:
        return "Email and password are required.", 400

    if password != repassword:
        return "Incorrect repass", 400

    user = Users.query.filter_by(email=email).first()
    if user is None:
        new_user = Users(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return "User sucessfully added", 200
    else:
        return "User already exists", 400