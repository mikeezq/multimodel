from datetime import datetime
from hashlib import md5

from flask_bcrypt import generate_password_hash, check_password_hash

from app.databases import postgre_repo


def signin(request_form):
    email = request_form.get('email')
    password = request_form.get('password')
    if not email or not password:
        return "Email and password are required.", 400, None

    user = postgre_repo.get_user_by_email(email)
    if user and check_password_hash(user.password, password):
        return "Logged in successfully!", 200, user.username
    else:
        return "Failed to login!", 400, None


def signup(request_form):
    postgre_repo.update_id_seq() # TODO: call only once
    email = request_form.get('email')
    password = request_form.get('password')
    password = generate_password_hash(password).decode('utf-8')
    repassword = request_form.get('repassword')
    repassword = generate_password_hash(repassword).decode('utf-8')
    username = request_form.get('username')

    if not email or not password:
        return "Email and password are required.", 400

    if password != repassword:
        return "Incorrect repass", 400

    user_by_email = postgre_repo.get_user_by_email(email)
    user_by_username = postgre_repo.get_user_by_username(username)
    if user_by_email is None and user_by_username is None:
        registration_date = datetime.now().date()
        print(registration_date)
        postgre_repo.create_new_user(username, password, email, registration_date)
        return "User sucessfully added", 200
    else:
        return f"User with such {email if user_by_email else username} already exists", 400
