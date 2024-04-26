from sqlalchemy import text

from app.models.users import Users
from app.models.movies import Movies


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

    def create_new_user(self, username, password, email, registration_date):
        new_user = Users(
            username=username,
            password=password,
            email=email,
            registration_date=registration_date
        )
        self.db.session.add(new_user)
        self.db.session.commit()

    def get_all_movies(self):
        movies = Movies.query.all()
        print(movies)
        return movies
