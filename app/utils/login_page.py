from app.databases import db_repo


def signin(request_form):
    email = request_form.get('email')
    password = request_form.get('password')
    if not email or not password:
        return "Email and password are required.", 400, None

    user = db_repo.get_user_by_email(email)
    if user and user.password == password:
        return "Logged in successfully!", 200, user.username
    else:
        return "Failed to login!", 400, None


def signup(request_form):
    db_repo.update_id_seq() # TODO: call only once
    email = request_form.get('email')
    password = request_form.get('password')
    repassword = request_form.get('repassword')
    username = request_form.get('username')

    if not email or not password:
        return "Email and password are required.", 400

    if password != repassword:
        return "Incorrect repass", 400

    user = db_repo.get_user_by_email(email)
    if user is None:
        db_repo.create_new_user(username, password, email)
        return "User sucessfully added", 200
    else:
        return "User already exists", 400