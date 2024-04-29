from flask import session, redirect, url_for

from app.databases import postgre_repo, mongo_repo, db
from app.s3.s3 import get_s3, bucket_name, get_presigned_url
from app.models.tv_shows import TV_Shows, TV_ShowDirectors, TV_ShowActors, TV_ShowGenres, Studios,\
    Genres, Directors, Actors


def create_serial_view(request):
    if session['role'] == 'user':
        redirect(url_for('main'))

    title = request.form['title']
    release_date = request.form['release_date']
    studio_name = request.form['studio_name']
    genre = request.form['genre']
    director = request.form['director_name']
    actor = request.form['actors']
    duration = request.form['duration']
    role = request.form['role']
    description = request.form['description']
    image = request.files['image']

    show_id = postgre_repo.get_last_show_id() + 1
    studio_id = Studios.query.filter(Studios.name == studio_name).first().studio_id
    tv_show = TV_Shows(show_id=show_id, title=title, release_date=release_date,
                       duration=duration, genre=genre, studio_id=studio_id, description=description)

    director_id = Directors.query.filter(Directors.name == director).first().director_id
    tv_show_directors = TV_ShowDirectors(show_id=show_id, director_id=director_id)

    genre_id = Genres.query.filter(Genres.name == genre).first().genre_id
    tv_show_genres = TV_ShowGenres(show_id=show_id, genre_id=genre_id)

    actor_id = Actors.query.filter(Actors.name == actor).first().actor_id
    tv_show_actors = TV_ShowActors(show_id=show_id, actor_id=actor_id, role=role)

    db.session.add(tv_show)
    db.session.commit()
    db.session.add(tv_show_directors)
    db.session.commit()
    db.session.add(tv_show_genres)
    db.session.commit()
    db.session.add(tv_show_actors)
    db.session.commit()

    get_s3().upload_fileobj(image, bucket_name, f"{title}.jpg")
    mongo_repo.create_show({"title": title, "link": get_presigned_url(f"{title}.jpg")})

    return redirect(url_for('index'))