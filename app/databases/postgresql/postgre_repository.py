from sqlalchemy import text

from app.models.users import Users, Reviews, Privileged_Users
from app.models.tv_shows import TV_Shows


reset_sequence_sql_users = text("""
    SELECT setval('users_user_id_seq', (SELECT MAX(user_id) FROM users));
""")

reset_sequence_sql_privileged_users = text("""
    SELECT setval('privileged_users_user_id_seq', (SELECT MAX(user_id) FROM users));
""")

get_film_info_sql = text("""
SELECT tv_shows.*,
       studios.name as studio_name,
       studios.country,
       d.name as director_name,
       string_agg(a2.name, ', ') as actors
FROM tv_shows
JOIN
studios on tv_shows.studio_id = studios.studio_id
JOIN
    tv_show_directors tsd on tv_shows.show_id = tsd.show_id
JOIN
    directors d on tsd.director_id = d.director_id
JOIN
    tv_show_actors a on tv_shows.show_id = a.show_id
JOIN
    actors a2 on a2.actor_id = a.actor_id
WHERE tv_shows.title = :title
GROUP BY tv_shows.show_id, studio_name, studios.country, d.name
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

    def get_show_reviews(self, title):
        shows = self.db.session.query(
            Users.user_id,
            Users.username,
            Reviews.rating,
            TV_Shows.title,
            Reviews.comment,
            Reviews.review_date
        ).join(
            Reviews, Users.user_id == Reviews.user_id
        ).join(
            TV_Shows, Reviews.show_id == TV_Shows.show_id
        ).filter(
            TV_Shows.title == title
        ).all()

        return shows

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

    def get_show_info(self, title):
        params = {'title': title}
        result = self.db.session.execute(get_film_info_sql, params)
        show_info = result.fetchall()
        return show_info[0]
