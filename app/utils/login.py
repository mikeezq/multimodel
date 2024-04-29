from datetime import datetime

from flask import flash
from flask_bcrypt import generate_password_hash, check_password_hash

from app.databases import postgre_repo


def signin(request_form):
    email = request_form.get('email')
    password = request_form.get('password')
    if not email or not password:
        flash('Email и пароль обязательны.', 'error')
        return "Email и пароль обязательны.", 400, None

    user = postgre_repo.get_user_by_email(email)
    if user and check_password_hash(user.password, password):
        return "Успешно!", 200, user.username
    else:
        flash('Неправильный пароль.', 'error')
        return "Неправильный пароль", 400, None


def signup(request_form):
    postgre_repo.update_id_seq() # TODO: call only once
    email = request_form.get('email')
    password = request_form.get('password').strip()
    repassword = request_form.get('repassword').strip()
    username = request_form.get('username')

    if not email or not password:
        flash(f"Email и пароль обязательны.", 'error')
        return "Email и пароль обязательны.", 400

    if password != repassword:
        flash(f"Неправильный повторный ввод пароля", 'error')
        return "Неправильный повторный ввод пароля", 400

    if not username:
        flash("Логин обязателен", "error")
        return "Логин обязателен", 400

    user_by_email = postgre_repo.get_user_by_email(email)
    user_by_username = postgre_repo.get_user_by_username(username)
    if user_by_email is None and user_by_username is None:
        registration_date = datetime.now().date()
        print(registration_date)
        password = generate_password_hash(password).decode('utf-8')
        postgre_repo.create_new_user(username, password, email, registration_date)
        flash(f"Пользователь успешно добавлен", 'success')
        return "Пользователь успешно добавлен", 200
    else:
        flash(f"Пользователь {email if user_by_email else username} уже существует", 'error')
        return f"Пользователь {email if user_by_email else username} уже существует", 400
