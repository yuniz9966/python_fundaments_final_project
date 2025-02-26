import sqlite3


def initialize_sqlite_db():
    with sqlite3.connect('search_queries.db') as connection:
        connection.execute('''
        CREATE TABLE IF NOT EXISTS search_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            param_key TEXT NOT NULL,
            count_queries INTEGER NOT NULL DEFAULT 1,
            `date` DATETIME DEFAULT CURRENT_TIMESTAMP,
            sql_query TEXT NOT NULL
        )
        ''')



def save_search_query(params, query_param=""):
    if len(params.split()) > 1:
         query_param = query_param % tuple(params.split())
    else:
        query_param = query_param % f"'%{params}%'"
    with sqlite3.connect('search_queries.db') as connection:
        cursor = connection.execute('SELECT id FROM search_queries WHERE param_key = ?', (params,))
        result = cursor.fetchone()
        if result:
            connection.execute('UPDATE search_queries SET count_queries = count_queries + 1 WHERE id = ?', (result[0],))
        else:
            connection.execute('INSERT INTO search_queries (param_key, count_queries, sql_query) VALUES (?, 1, ?)', (params, query_param.lstrip('\n')))


def get_popular_search_queries():
    with sqlite3.connect('search_queries.db') as connection:
        cursor = connection.execute('''
        SELECT param_key, count_queries
        FROM search_queries
        ORDER BY count_queries DESC
        LIMIT 5
        ''')
        return cursor.fetchall()





