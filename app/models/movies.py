from app.databases import db


class Movies(db.Model):
    __tablename__ = 'Movies'

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    duration = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    studio_id = db.Column(db.Integer, db.ForeignKey('Studios.studio_id'))


class Studios(db.Model):
    __tablename__ = 'studios'

    studio_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50))
    foundation_date = db.Column(db.Date)


class Directors(db.Model):
    __tablename__ = 'directors'

    director_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(50))
    birth_date = db.Column(db.Date)


class Actors(db.Model):
    __tablename__ = 'actors'

    actor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(50))
    birth_date = db.Column(db.Date)


class MovieDirectors(db.Model):
    __tablename__ = 'movie_directors'

    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'), primary_key=True)
    director_id = db.Column(db.Integer, db.ForeignKey('Directors.director_id'), primary_key=True)


class MovieActors(db.Model):
    __tablename__ = 'movie_actors'

    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actors.actor_id'), primary_key=True)
    role = db.Column(db.String(100))


class Genres(db.Model):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class MovieGenres(db.Model):
    __tablename__ = 'movie_genres'

    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('Genres.genre_id'), primary_key=True)


class Collections(db.Model):
    __tablename__ = 'collections'

    collection_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)


class CollectionMovies(db.Model):
    __tablename__ = 'collection_movies'

    collection_id = db.Column(db.Integer, db.ForeignKey('Collections.collection_id'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'), primary_key=True)


class TrailerViews(db.Model):
    __tablename__ = 'trailer_views'

    view_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'))
    view_date = db.Column(db.Date)
