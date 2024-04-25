-- Таблица с информацией о студиях
CREATE TABLE Studios (
    studio_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50),
    foundation_date DATE
);

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

-- Таблица с информацией о пользователе
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255),
    registration_date DATE
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
    session_id SERIAL PRIMARY KEY,
    user_id INT,
    login_time DATE,
    logout_time DATE,
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

-- Вставка данных в таблицу Studios
INSERT INTO Studios (studio_id, name, country, foundation_date)
VALUES (1, 'Warner Bros. Pictures', 'США', '1923-04-04'),
       (2, '20th Century Fox', 'США', '1935-05-31'),
       (3, 'Castle Rock Entertainment', 'США', '1987-06-03'),
       (4, 'New Line Cinema', 'США', '1967-08-15'),
       (5, 'Regency Enterprises', 'США', '1982-11-10'),
       (6, 'Syncopy', 'США', '2001-01-01');

-- Вставка данных в таблицу Directors
INSERT INTO Directors (director_id, name, nationality, birth_date)
VALUES (1, 'Кристофер Нолан', 'Британия', '1970-07-30'),
       (2, 'Джордж Лукас', 'США', '1944-05-14'),
       (3, 'Фрэнк Дарабонт', 'США', '1959-01-28'),
       (4, 'Питер Джексон', 'Новая Зеландия', '1961-10-31'),
       (5, 'Дэвид Финчер', 'США', '1962-08-28');
	   (6, 'Куентин Тарантино', 'США', '1963-03-27');

-- Вставка данных в таблицу Actors
INSERT INTO Actors (actor_id, name, nationality, birth_date)
VALUES (1, 'Леонардо ДиКаприо', 'США', '1974-11-11'),
       (2, 'Харрисон Форд', 'США', '1942-07-13'),
       (3, 'Тим Роббинс', 'США', '1958-10-16'),
       (4, 'Вигго Мортенсен', 'США', '1958-10-20'),
       (5, 'Брэд Питт', 'США', '1963-12-18');
	   (6, 'Мэттью Макконахи', 'США', '1969-11-04');

-- Вставка данных в таблицу Movies
INSERT INTO Movies (movie_id, title, release_date, duration, genre, studio_id)
VALUES (1, 'Начало', '2010-07-16', 148, 'фантастика, боевик', 1),
       (2, 'Звёздные войны: Эпизод 4 – Новая надежда', '1977-05-25', 121, 'фантастика, боевик', 2),
       (3, 'Побег из Шоушенка', '1994-10-14', 142, 'драма', 3),
       (4, 'Властелин колец: Возвращение короля', '2003-12-17', 201, 'фэнтези, приключения', 4),
       (5, 'Бойцовский клуб', '1999-10-15', 139, 'драма, триллер', 5),
       (6, 'Темный рыцарь', '2008-07-18', 152, 'боевик, криминал, драма', 6);

-- Вставка данных в таблицу Movie_Directors
INSERT INTO Movie_Directors (movie_id, director_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 1);

-- Вставка данных в таблицу Movie_Actors
INSERT INTO Movie_Actors (movie_id, actor_id, ROLE)
VALUES (1, 1, 'Dominic Cobb'),
       (1, 2, 'Cobb'),
       (2, 2, 'Han Solo'),
       (3, 3, 'Andy Dufresne'),
       (3, 4, 'Red'),
       (4, 4, 'Aragorn'),
       (5, 5, 'Tyler Durden'),
       (6, 1, 'Bruce Wayne');

-- Вставка данных в таблицу Users
INSERT INTO Users (user_id, username, email, password, registration_date)
VALUES (1, 'user1', 'user1@example.com', 'password1', '2024-04-25'),
       (2, 'user2', 'user2@example.com', 'password2', '2024-04-25'),
       (3, 'user3', 'user3@example.com', 'password3', '2024-04-25');

-- Вставка данных в таблицу Reviews
INSERT INTO Reviews (review_id, movie_id, user_id, rating, comment, review_date)
VALUES (1, 1, 1, 9.5, 'Отличный фильм!', '2024-04-25'),
       (2, 2, 1, 8.7, 'Классика жанра.', '2024-04-25'),
       (3, 3, 2, 10, 'Лучший фильм всех времен.', '2024-04-25');

-- Вставка данных в таблицу Genres
INSERT INTO Genres (genre_id, name)
VALUES (1, 'фантастика'),
       (2, 'боевик'),
       (3, 'драма'),
       (4, 'приключения'),
       (5, 'триллер'),
       (6, 'криминал');

-- Вставка данных в таблицу Movie_Genres
INSERT INTO Movie_Genres (movie_id, genre_id)
VALUES (1, 1),
       (1, 2),
       (2, 1),
       (2, 2),
       (3, 3),
       (4, 1),
       (4, 4),
       (5, 3),
       (5, 5),
       (6, 2),
       (6, 6);

-- Вставка данных в таблицу Collections
INSERT INTO Collections (collection_id, name, description)
VALUES (1, 'Лучшие фильмы', 'Коллекция лучших фильмов всех времен'),
       (2, 'Фильмы про любовь', 'Коллекция фильмов о любви и романтике');

-- Вставка данных в таблицу Collection_Movies
INSERT INTO Collection_Movies (collection_id, movie_id)
VALUES (1, 1),
       (1, 3),
       (1, 4),
       (1, 6),
       (2, 3),
       (2, 5);

-- Вставка данных в таблицу Wishlists
INSERT INTO Wishlists (wishlist_id, user_id, movie_id)
VALUES (1, 1, 2),
       (2, 1, 5),
       (3, 2, 4);

-- Вставка данных в таблицу Watchedlist
INSERT INTO Watchedlist (watched_id, user_id, movie_id, watched_date)
VALUES (1, 1, 1, '2024-04-25'),
       (2, 1, 3, '2024-04-25'),
       (3, 1, 6, '2024-04-25'),
       (4, 2, 2, '2024-04-25');

-- Вставка данных в таблицу Sessions
INSERT INTO Sessions (session_id, user_id, login_time, logout_time)
VALUES (1, 1, '2024-04-25 10:00:00', '2024-04-25 11:00:00'),
       (2, 2, '2024-04-25 09:00:00', '2024-04-25 10:30:00');

-- Вставка данных в таблицу Payments
INSERT INTO Payments (payment_id, user_id, amount, payment_date)
VALUES (1, 1, 10.99, '2024-04-25'),
       (2, 2, 5.99, '2024-04-25');

-- Вставка данных в таблицу Subscriptions
INSERT INTO Subscriptions (subscription_id, user_id, plan, start_date, end_date)
VALUES (1, 1, 'Premium', '2024-04-25', '2024-05-25'),
       (2, 2, 'Basic', '2024-04-25', '2024-05-25');

-- Вставка данных в таблицу Trailer_Views
INSERT INTO Trailer_Views (view_id, user_id, movie_id, view_date)
VALUES (1, 1, 1, '2024-04-25'),
       (2, 1, 2, '2024-04-25'),
       (3, 2, 3, '2024-04-25');
