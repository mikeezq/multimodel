-- Таблица с информацией о студиях
CREATE TABLE Studios (
    studio_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50),
    foundation_date DATE
);

-- Вставка данных в таблицу Studios
INSERT INTO Studios (studio_id, name, country, foundation_date)
VALUES (1, 'Warner Bros. Pictures', 'США', '1923-04-04'),
       (2, '20th Century Fox', 'США', '1935-05-31'),
       (3, 'Castle Rock Entertainment', 'США', '1987-06-03'),
       (4, 'New Line Cinema', 'США', '1967-08-15'),
       (5, 'Regency Enterprises', 'США', '1982-11-10'),
       (6, 'Syncopy', 'США', '2001-01-01'),
       (7, 'FX', 'США', '2002-03-12');

-- Таблица с информацией о тв сериалах
CREATE TABLE TV_Shows (
    show_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_date DATE,
    duration VARCHAR(50),
    genre VARCHAR(50),
    studio_id INT,
    description varchar(5000),
    FOREIGN KEY (studio_id) REFERENCES Studios(studio_id)
);

-- Вставка данных в таблицу TV_Shows
INSERT INTO TV_Shows (show_id, title, release_date, duration, genre, studio_id, description)
VALUES
    (1, 'Игра престолов', '2011-04-17', '2 дня 18 часов 55 минут', 'фэнтези, драма, приключения', 2, 'К концу подходит время благоденствия, и лето, длившееся почти десятилетие, угасает. Вокруг средоточия власти Семи королевств, Железного трона, зреет заговор, и в это непростое время король решает искать поддержки у друга юности Эддарда Старка. В мире, где все — от короля до наемника — рвутся к власти, плетут интриги и готовы вонзить нож в спину, есть место и благородству, состраданию и любви. Между тем никто не замечает пробуждение тьмы из легенд далеко на Севере — и лишь Стена защищает живых к югу от нее.'),
    (2, 'Друзья', '1994-09-22', '3 дня 18 часов 11 минут', 'комедия, мелодрама', 1, 'Шестеро друзей – Рейчел, Моника, Фиби, Джоуи, Чендлер и Росс – живут по соседству, вместе убивают время, делятся секретами и иногда очень сильно влюбляются.'),
    (3, 'Шерлок', '2010-07-25', '22 часа 7 минут', 'детектив, драма', 3, 'События разворачиваются в наши дни. Он прошел Афганистан, остался инвалидом. По возвращении в родные края встречается с загадочным, но своеобразным гениальным человеком. Тот в поиске соседа по квартире. Лондон, 2010 год. Происходят необъяснимые убийства. Скотланд-Ярд без понятия, за что хвататься. Существует лишь один человек, который в силах разрешить проблемы и найти ответы на сложные вопросы.'),
    (4, 'Во все тяжкие', '2008-01-20', '2 дня 2 часа 37 минут', 'драма, криминал, триллер', 4, 'Школьный учитель химии Уолтер Уайт узнаёт, что болен раком лёгких. Учитывая сложное финансовое состояние дел семьи, а также перспективы, Уолтер решает заняться изготовлением метамфетамина. Для этого он привлекает своего бывшего ученика Джесси Пинкмана, когда-то исключённого из школы при активном содействии Уайта. Пинкман сам занимался варкой мета, но накануне, в ходе рейда УБН, он лишился подельника и лаборатории.'),
    (5, 'Черное зеркало', '2011-12-04', '1 день 4 часа 9 минут', 'научная фантастика, драма, триллер', 5, 'За последние годы технологии всесторонне изменили нашу жизнь, прежде чем мы успели опомниться и усомниться в них. В каждом доме, на каждом столе, на каждой ладони — плазменный телевизор, монитор компьютера, дисплей смартфона — чёрное зеркало нашего существования в XXI веке.'),
    (6, 'Карточный домик', '2013-02-01', '2 дня 13 часов 55 минут', 'драма, триллер', 6, 'Амбициозный конгрессмен от Демократической партии Фрэнк Андервуд в обмен на обещание сделать его госсекретарём помогает Гаррету Уокеру стать президентом США. Однако после выборов глава администрации президента Линда Васкес сообщает Андервуду, что он не получит должность. Взбешенные предательством Фрэнк и его жена готовы пойти на всё, чтобы отомстить новоиспечённому президенту.');

-- Таблица с информацией о пользователе
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255),
    registration_date DATE
);

-- Вставка данных в таблицу Users
INSERT INTO Users (user_id, username, email, password, registration_date)
VALUES (1, 'user1', 'user1', 'password1', '2024-04-25'),
       (2, 'user2', 'user2', 'password2', '2024-04-25'),
       (3, 'test', 'test', 'test', '2024-04-25'),
       (4, 'user3', 'user3', 'password3', '2024-04-25'),
       (5, 'admin', 'admin', 'admin', '2024-04-25'),
       (6, 'moder1', 'moder1', 'moder1', '2024-04-25'),
       (7, 'moder2', 'moder2', 'moder2', '2024-04-25');

-- Таблица с информацией о режиссерах
CREATE TABLE Directors (
    director_id INT PRIMARY KEY,
    name VARCHAR(100),
    nationality VARCHAR(50),
    birth_date DATE
);

-- Вставка данных в таблицу Directors
INSERT INTO Directors (director_id, name, nationality, birth_date)
VALUES
    (1, 'Дэвид Бениофф', 'США', '1970-09-25'),
    (2, 'Дэнни Кэннон', 'США', '1975-08-19'),
    (3, 'Мигель Сапочник', 'США', '1974-05-16'),
    (4, 'Том Маккарти', 'США', '1969-06-22'),
    (5, 'Алекс Грейвз', 'Великобритания', '1977-02-14');


-- Таблица с информацией о актерах
CREATE TABLE Actors (
    actor_id INT PRIMARY KEY,
    name VARCHAR(100),
    nationality VARCHAR(50),
    birth_date DATE
);

-- Вставка данных в таблицу Actors
INSERT INTO Actors (actor_id, name, nationality, birth_date)
VALUES
    (1, 'Кит Хэрингтон', 'Великобритания', '1986-12-26'),
    (2, 'Эмилия Кларк', 'Великобритания', '1986-10-23'),
    (3, 'Дженнифер Энистон', 'США', '1969-02-11'),
    (4, 'Кортни Кокс', 'США', '1964-06-15'),
    (5, 'Бенедикт Камбербэтч', 'Великобритания', '1976-07-19'),
    (6, 'Брайан Крэнстон', 'США', '1956-03-07'),
    (7, 'Чарли Брукер', 'Великобритания', '1971-03-03'),
    (8, 'Кевин Спейси', 'США', '1959-07-26');

-- Таблица, связывающая тв сериал и их режиссеров (многие ко многим)
CREATE TABLE TV_Show_Directors (
    show_id INT,
    director_id INT,
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id),
    FOREIGN KEY (director_id) REFERENCES Directors(director_id),
    PRIMARY KEY (show_id, director_id)
);

-- Вставка данных в таблицу TV_Show_Directors
INSERT INTO TV_Show_Directors (show_id, director_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 1);

-- Таблица, связывающая тв сериал и их актеров (многие ко многим)
CREATE TABLE TV_Show_Actors (
    show_id INT,
    actor_id INT,
    role VARCHAR(100),
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id),
    FOREIGN KEY (actor_id) REFERENCES Actors(actor_id),
    PRIMARY KEY (show_id, actor_id)
);

-- Вставка данных в таблицу TV_Show_Actors
INSERT INTO TV_Show_Actors (show_id, actor_id, ROLE)
VALUES (1, 1, 'Jon Snow'),
    (1, 2, 'Daenerys Targaryen'),
    (2, 3, 'Rachel Green'),
    (2, 4, 'Monica Geller'),
    (3, 5, 'Sherlock Holmes'),
    (3, 6, 'John Watson'),
    (4, 7, 'Walter White'),
    (5, 8, 'Narrator'),
    (6, 1, 'Frank Underwood');

-- Таблица с отзывами пользователей о тв сериалах
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    show_id INT,
    user_id INT,
    rating DECIMAL(3, 1),
    comment TEXT,
    review_date DATE,
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Вставка данных в таблицу Reviews
INSERT INTO Reviews (review_id, show_id, user_id, rating, comment, review_date)
VALUES (1, 1, 1, 9.5, 'Отличный сериал!', '2024-04-25'),
       (2, 2, 1, 8.7, 'Классика жанра.', '2024-04-25'),
       (3, 3, 2, 10, 'Лучший тв сериал всех времен.', '2024-04-25');

-- Таблица с информацией о жанрах
CREATE TABLE Genres (
    genre_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Вставка данных в таблицу Genres
INSERT INTO Genres (genre_id, name)
VALUES     (1, 'фэнтези'),
    (2, 'драма'),
    (3, 'приключения'),
    (4, 'комедия'),
    (5, 'мелодрама'),
    (6, 'детектив'),
    (7, 'триллер'),
    (8, 'научная фантастика'),
    (9, 'криминал');

-- Таблица, связывающая тв сериал и их жанры (многие ко многим)
CREATE TABLE TV_Show_Genres (
    show_id INT,
    genre_id INT,
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id),
    PRIMARY KEY (show_id, genre_id)
);

-- Вставка данных в таблицу TV_Show_Genres
INSERT INTO TV_Show_Genres (show_id, genre_id)
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

-- Таблица с информацией о коллекциях тв сериалах
CREATE TABLE Collections (
    collection_id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

-- Вставка данных в таблицу Collections
INSERT INTO Collections (collection_id, name, description)
VALUES (1, 'Лучшие тв сериалы', 'Коллекция лучших тв сериалов всех времен'),
       (2, 'ТВ сериалы про любовь', 'Коллекция фильмов о любви и романтике');

-- Таблица, связывающая коллекции и тв сериалы (многие ко многим)
CREATE TABLE Collection_TV_Shows (
    collection_id INT,
    show_id INT,
    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id),
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id),
    PRIMARY KEY (collection_id, show_id)
);

-- Вставка данных в таблицу Collection_TV_Shows
INSERT INTO Collection_TV_Shows (collection_id, show_id)
VALUES (1, 1),
       (1, 3),
       (1, 4),
       (1, 6),
       (2, 3),
       (2, 5);


-- Таблица с информацией о списке желаемых тв сериалов пользователей
CREATE TABLE Wishlists (
    wishlist_id INT PRIMARY KEY,
    user_id INT,
    show_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id)
);

-- Вставка данных в таблицу Wishlists
INSERT INTO Wishlists (wishlist_id, user_id, show_id)
VALUES (1, 1, 2),
       (2, 1, 5),
       (3, 2, 4);

-- Таблица с информацией о списке просмотренных тв сериалов пользователей
CREATE TABLE Watchedlist (
    watched_id INT PRIMARY KEY,
    user_id INT,
    show_id INT,
    watched_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id)
);

-- Вставка данных в таблицу Watchedlist
INSERT INTO Watchedlist (watched_id, user_id, show_id, watched_date)
VALUES (1, 1, 1, '2024-04-25'),
       (2, 1, 3, '2024-04-25'),
       (3, 1, 6, '2024-04-25'),
       (4, 2, 2, '2024-04-25');

-- Таблица с информацией о сессиях пользователей
CREATE TABLE Sessions (
    session_id SERIAL PRIMARY KEY,
    user_id INT,
    login_time DATE,
    logout_time DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Вставка данных в таблицу Sessions
INSERT INTO Sessions (session_id, user_id, login_time, logout_time)
VALUES (1, 1, '2024-04-25 10:00:00', '2024-04-25 11:00:00'),
       (2, 2, '2024-04-25 09:00:00', '2024-04-25 10:30:00');

-- Таблица с информацией о платежах пользователей
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Вставка данных в таблицу Payments
INSERT INTO Payments (payment_id, user_id, amount, payment_date)
VALUES (1, 1, 10.99, '2024-04-25'),
       (2, 2, 5.99, '2024-04-25');

-- Таблица с информацией о подписках пользователей
CREATE TABLE Subscriptions (
    subscription_id INT PRIMARY KEY,
    user_id INT,
    plan VARCHAR(50),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Вставка данных в таблицу Subscriptions
INSERT INTO Subscriptions (subscription_id, user_id, plan, start_date, end_date)
VALUES (1, 1, 'Premium', '2024-04-25', '2024-05-25'),
       (2, 2, 'Basic', '2024-04-25', '2024-05-25');


-- Таблица с информацией о просмотренных пользователем трейлерах тв сериалов
CREATE TABLE Trailer_Views (
    view_id INT PRIMARY KEY,
    user_id INT,
    show_id INT,
    view_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (show_id) REFERENCES TV_Shows(show_id)
);

-- Вставка данных в таблицу Trailer_Views
INSERT INTO Trailer_Views (view_id, user_id, show_id, view_date)
VALUES (1, 1, 1, '2024-04-25'),
       (2, 1, 2, '2024-04-25'),
       (3, 2, 3, '2024-04-25');


create type roles as enum ('moderator', 'admin');
-- Таблица с информацией о пользователях с привилегиями
CREATE TABLE Privileged_Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255),
    registration_date DATE,
    role roles
);

-- Вставка данных в таблицу Users
INSERT INTO Privileged_Users (user_id, username, email, password, registration_date, role)
VALUES (1, 'admin', 'admin', 'admin', '2024-04-25', 'admin'),
       (2, 'moder1', 'moder1', 'moder1', '2024-04-26', 'moderator'),
       (3, 'moder2', 'moder2', 'moder2', '2024-04-27', 'moderator');
