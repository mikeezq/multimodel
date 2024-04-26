from app.models.users import Users
from sqlalchemy import text


reset_sequence_sql = text("""
    SELECT setval('users_user_id_seq', (SELECT MAX(user_id) FROM users));
""")


class Db_Repository:
    def __init__(self, db):
        self.db = db

    def update_id_seq(self):
        self.db.session.execute(reset_sequence_sql)
        self.db.session.commit()

    def get_user_by_email(self, email):
        return Users.query.filter_by(email=email).first()

    def create_new_user(self, username, password, email):
        new_user = Users(username=username, password=password, email=email)
        self.db.session.add(new_user)
        self.db.session.commit()
