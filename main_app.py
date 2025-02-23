from sakila_queries import connect_to_db, search_movies_by_keyword, search_movies_by_genre_and_year
from local_save_queries import initialize_sqlite_db, save_search_query, get_popular_search_queries


# ANSI коды для изменения цвета и стиля текста
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"

BOLD = "\033[1m"
YELLOW_UNDERLINE = "\033[33;4m"
BOLD_GREEN_BACKGROUND = "\033[1;42m"


def print_formated(text, format):
    print(f"{format}{text}{RESET}")




def main():
    connect = connect_to_db()
    if connect:
        print()
        print_formated("Соединение с базой данных MySQL УСТАНОВЛЕНО.", BOLD_GREEN_BACKGROUND)

    initialize_sqlite_db()

    while True:
        print_formated("\nВыберите действие:", YELLOW_UNDERLINE)
        print_formated("1. Поиск фильмов по ключевому слову", BOLD)
        print_formated("2. Поиск фильмов по жанру и году", BOLD)
        print_formated("3. Показать самые популярные запросы", BOLD)
        print_formated("4. Выйти", BOLD)

        choice = input("\nВведите номер действия: ")

        if choice == "1":
            keyword = input("Введите ключевое слово для поиска фильмов: ")
            movies = search_movies_by_keyword(keyword)
            save_search_query(keyword)
            display_movies(movies)

        elif choice == "2":
            genre = input("Введите жанр: ")
            year = input("Введите год: ")
            movies = search_movies_by_genre_and_year(genre, year)
            save_search_query(f"{genre} {year}")
            display_movies(movies)

        elif choice == "3":
            queries = get_popular_search_queries()
            display_popular_queries(queries)

        elif choice == "4":
            print_formated("Выход из программы.", RED)
            break

        else:
            print_formated("Неверный выбор. Пожалуйста, попробуйте снова.", RED)

def display_movies(movies):
    if movies:
        print_formated(f"\nНайдено фильмов: {len(movies)}", GREEN)
        for movie in movies:
            print(f'Название: "{movie.get("title")}",  Год выпуска: {movie.get("release_year")}')
    else:
        print_formated("\nФильмы не найдены.", RED)

def display_popular_queries(queries):
    if queries:
        print_formated("Самые популярные запросы:", GREEN)
        for query in queries:
            print(f"Запрос: {query[0]}, Количество: {query[1]}")
    else:
        print_formated("\nПопулярные запросы не найдены.", RED)

if __name__ == "__main__":
    main()
