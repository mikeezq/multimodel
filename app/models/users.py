from app.databases import db


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.Date, nullable=True)


class Reviews(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    rating = db.Column(db.Numeric(3, 1))
    comment = db.Column(db.Text)
    review_date = db.Column(db.Date)


class Wishlists(db.Model):
    __tablename__ = 'wishlists'

    wishlist_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'))


class Watchedlist(db.Model):
    __tablename__ = 'watchedlist'

    watched_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'))
    watched_date = db.Column(db.Date)


class Sessions(db.Model):
    __tablename__ = 'sessions'

    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    login_time = db.Column(db.DateTime)
    logout_time = db.Column(db.DateTime)


class Payments(db.Model):
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    amount = db.Column(db.Numeric(10, 2))
    payment_date = db.Column(db.Date)


class Subscriptions(db.Model):
    __tablename__ = 'subscriptions'

    subscription_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    plan = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)


