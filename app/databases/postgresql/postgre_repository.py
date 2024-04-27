from sqlalchemy import text

from app.models.users import Users, Reviews, Privileged_Users
from app.models.tv_shows import TV_Shows


reset_sequence_sql_users = text("""
    SELECT setval('users_user_id_seq', (SELECT MAX(user_id) FROM users));
""")

reset_sequence_sql_privileged_users = text("""
    SELECT setval('privileged_users_user_id_seq', (SELECT MAX(user_id) FROM users));
""")


class Postgre_Repository:
    def __init__(self, db):
        self.db = db

    def update_id_seq(self):
        self.db.session.execute(reset_sequence_sql_users)
        self.db.session.execute(reset_sequence_sql_privileged_users)
        self.db.session.commit()

    def get_user_by_email(self, email):
        return Users.query.filter_by(email=email).first()

    def create_new_user(self, username, password, email, registration_date):
        new_user = Users(
            username=username,
            password=password,
            email=email,
            registration_date=registration_date
        )
        self.db.session.add(new_user)
        self.db.session.commit()

    def get_all_shows(self):
        shows = TV_Shows.query.all()
        return shows

    def get_user_reviews(self, username="user1"):
        reviews = self.db.session.query(
            Users.user_id,
            Reviews.rating,
            TV_Shows.title,
            Reviews.comment,
            Reviews.review_date
        ).join(
            Reviews, Users.user_id == Reviews.user_id
        ).join(
            TV_Shows, Reviews.show_id == TV_Shows.show_id
        ).filter(
            Users.username == username
        ).all()

        return reviews

    def get_privileged_users(self):
        admins = self.db.session.query(
            Privileged_Users.username,
        ).filter(
            Privileged_Users.role == "admin"
        ).all()
        print(admins)

        moderators = self.db.session.query(
            Privileged_Users.username,
        ).filter(
            Privileged_Users.role == "moderator"
        ).all()
        print(moderators)

        return admins, moderators
