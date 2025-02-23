import pymysql
from config import dbconfig

def connect_to_db():
    try:
        connection = pymysql.connect(**dbconfig)
        return connection
    except pymysql.MySQLError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def search_movies_by_keyword(keyword):
    connection = connect_to_db()
    if connection is None:
        return None

    try:
        with connection.cursor() as cursor:
            sql_query = """
            SELECT title, release_year FROM film
            WHERE concat(title, description) LIKE %s 
            LIMIT 10
            """
            search_term = f"%{keyword}%"
            cursor.execute(sql_query, (search_term,))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def search_movies_by_genre_and_year(genre, year):
    connection = connect_to_db()
    if connection is None:
        return None

    try:
        with connection.cursor() as cursor:
            sql_query = """
            SELECT f.* FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
            WHERE c.name = %s AND f.release_year = %s
            LIMIT 10
            """
            cursor.execute(sql_query, (genre, year))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()
