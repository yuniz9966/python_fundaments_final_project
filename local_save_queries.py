import sqlite3


def initialize_sqlite_db():
    with sqlite3.connect('search_queries.db') as connection:
        connection.execute('''
        CREATE TABLE IF NOT EXISTS search_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL UNIQUE,
            count_queries INTEGER NOT NULL DEFAULT 1,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')



def save_search_query(query):
    with sqlite3.connect('search_queries.db') as connection:
        cursor = connection.execute('SELECT id FROM search_queries WHERE query = ?', (query,))
        result = cursor.fetchone()

        if result:
            connection.execute('UPDATE search_queries SET count_queries = count_queries + 1 WHERE id = ?', (result[0],))
        else:
            connection.execute('INSERT INTO search_queries (query, count_queries) VALUES (?, 1)', (query,))

def get_popular_search_queries():
    with sqlite3.connect('search_queries.db') as connection:
        cursor = connection.execute('''
        SELECT query, count_queries
        FROM search_queries
        ORDER BY count_queries DESC
        LIMIT 10
        ''')
        return cursor.fetchall()

