-- Таблица с информацией о фильмах
CREATE TABLE Movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255),
    release_date DATE,
    duration INT,
    genre VARCHAR(50),
    studio_id INT,
    FOREIGN KEY (studio_id) REFERENCES Studios(studio_id)
);

-- Таблица с информацией о студиях
CREATE TABLE Studios (
    studio_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50),
    foundation_date DATE
);

-- Таблица с информацией о режиссерах
CREATE TABLE Directors (
    director_id INT PRIMARY KEY,
    name VARCHAR(100),
    nationality VARCHAR(50),
    birth_date DATE
);

-- Таблица с информацией о актерах
CREATE TABLE Actors (
    actor_id INT PRIMARY KEY,
    name VARCHAR(100),
    nationality VARCHAR(50),
    birth_date DATE
);

-- Таблица, связывающая фильмы и их режиссеров (многие ко многим)
CREATE TABLE Movie_Directors (
    movie_id INT,
    director_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (director_id) REFERENCES Directors(director_id),
    PRIMARY KEY (movie_id, director_id)
);

-- Таблица, связывающая фильмы и их актеров (многие ко многим)
CREATE TABLE Movie_Actors (
    movie_id INT,
    actor_id INT,
    role VARCHAR(100),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actors(actor_id),
    PRIMARY KEY (movie_id, actor_id)
);

-- Таблица с информацией о пользователе
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255),
    registration_date DATE
);

-- Таблица с отзывами пользователей о фильмах
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating DECIMAL(3, 1),
    comment TEXT,
    review_date DATE,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Таблица с информацией о жанрах
CREATE TABLE Genres (
    genre_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Таблица, связывающая фильмы и их жанры (многие ко многим)
CREATE TABLE Movie_Genres (
    movie_id INT,
    genre_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id),
    PRIMARY KEY (movie_id, genre_id)
);

-- Таблица с информацией о коллекциях фильмов
CREATE TABLE Collections (
    collection_id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

-- Таблица, связывающая коллекции и фильмы (многие ко многим)
CREATE TABLE Collection_Movies (
    collection_id INT,
    movie_id INT,
    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    PRIMARY KEY (collection_id, movie_id)
);

-- Таблица с информацией о списке желаемых фильмов пользователей
CREATE TABLE Wishlists (
    wishlist_id INT PRIMARY KEY,
    user_id INT,
    movie_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);

-- Таблица с информацией о списке просмотренных фильмов пользователей
CREATE TABLE Watchedlist (
    watched_id INT PRIMARY KEY,
    user_id INT,
    movie_id INT,
    watched_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);

-- Таблица с информацией о сессиях пользователей
CREATE TABLE Sessions (
    session_id INT PRIMARY KEY,
    user_id INT,
    login_time DATETIME,
    logout_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Таблица с информацией о платежах пользователей
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Таблица с информацией о подписках пользователей
CREATE TABLE Subscriptions (
    subscription_id INT PRIMARY KEY,
    user_id INT,
    plan VARCHAR(50),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Таблица с информацией о просмотренных пользователем трейлерах фильмов
CREATE TABLE Trailer_Views (
    view_id INT PRIMARY KEY,
    user_id INT,
    movie_id INT,
    view_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);
