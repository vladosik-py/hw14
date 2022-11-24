import json
import sqlite3


def get_movie_by_title(title):
    """выполняет поиск фильмов по названию"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title LIKE '%{title}%'
                    ORDER BY release_year DESC
                    """)

    data = cursor.fetchone()

    film = {
        "title": data[0],
        "country": data[1],
        "release_year": data[2],
        "genre": data[3],
        "description": data[4]
    }

    return film


def get_movie_by_years(year_1, year_2):
    """выполняет поиск фильмов по годам"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {year_1} and {year_2}
                    LIMIT 100
                    """)

    data = cursor.fetchall()

    films = []
    for i in data:
        film = {
            "title": i[0],
            "release_year": i[1]
        }

        films.append(film)

    return films


def get_movie_by_genre(genre):
    """выполняет поиск фильмов по жанру"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY release_year DESC
                    LIMIT 10
                    """)

    data = cursor.fetchall()

    films = []
    for i in data:
        film = {
            "title": i[0],
            "description": i[1]
        }

        films.append(film)

    return films


def rating_children():
    """выполняет поиск фильмов с рейтингом G"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G'
                    LIMIT 10
                    """)

    data = cursor.fetchall()

    films = []
    for i in data:
        film = {
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        }

        films.append(film)

    return films


def rating_family():
    """выполняет поиск фильмов с рейтингом G, PG, PG-13"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G' or rating = 'PG' or rating = 'PG-13'
                    LIMIT 10
                    """)

    data = cursor.fetchall()

    films = []
    for i in data:
        film = {
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        }

        films.append(film)

    return films


def rating_adults():
    """выполняет поиск фильмов с рейтингом R, NC-17"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute("""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'R' or rating = 'NC-17'
                    LIMIT 10
                    """)

    data = cursor.fetchall()

    films = []
    for i in data:
        film = {
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        }

        films.append(film)

    return films


def get_movie_by_cast(actor_1, actor_2):
    """выполняет поиск фильмов по актерскому составу"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT COUNT(netflix.cast), netflix.cast
                    FROM netflix
                    WHERE netflix.cast LIKE '%{actor_1}%' and netflix.cast LIKE '%{actor_2}%'
                    GROUP BY netflix.cast
                    """)

    return cursor.fetchall()


def search_for_movie(film_type, release_year, genre):
    """выполняет поиск фильмов по типу, году выпуска и жанру, и выводит описание"""
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT title, description
                    FROM netflix
                    WHERE type = '%{film_type}%' and release_year = '{release_year}' and listed_in LIKE '%{genre}%'
                    """)

    return cursor.fetchall()
