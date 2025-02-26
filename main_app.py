from sakila_queries import connect_to_db, search_movies_by_keyword, search_movies_by_genre_and_year
from local_save_queries import initialize_sqlite_db, save_search_query, get_popular_search_queries


# ANSI коды для изменения цвета и стиля текста
RESET = "\033[0m"
BOLD = "\033[1m"
BOLD_RED = "\033[1;31m"
BOLD_GREEN = "\033[1;32m"
BOLD_YELLOW_UNDERLINE = "\033[1;33;4m"
BOLD_GREEN_BACKGROUND = "\033[1;42m"


def print_formated(text, format):
    print(f"{format}{text}{RESET}")



def main():
    connect = connect_to_db()
    if connect:
        print()
        print_formated("☑️ Соединение с базой данных MySQL УСТАНОВЛЕНО", BOLD_GREEN_BACKGROUND)

    initialize_sqlite_db()

    while True:
        print_formated("\nЛегендарное меню действий! Выберите мудро:", BOLD_YELLOW_UNDERLINE)
        print_formated("1. Искать фильмы по ключевому слову (как настоящий детектив 🕵️‍♂️)", BOLD)
        print_formated("2. Искать фильмы по жанру и году (как квест, но полегче 🎬)", BOLD)
        print_formated("3. Посмотреть популярные запросы 🍿", BOLD)
        print_formated("4. Самоуничтожиться… шучу, просто выйти из программы 😎", BOLD)

        choice = input("\nВведите номер действия: ")

        if choice == "1":
            keyword = input("Введите ключевое слово для поиска фильмов: ").lower()
            movies, sql_query = search_movies_by_keyword(keyword)
            save_search_query(keyword, sql_query)
            display_movies(movies)

        elif choice == "2":
            print_formated("Список доступных жанров:", BOLD_YELLOW_UNDERLINE)
            print("Action, Animation, Children, Classics, Comedy, Documentary,"
                " Drama, \nFamily, Foreign, Games, Horror, Music, New, Sci-Fi, Sports, Travel")
            print_formated("Годы выпуска:", BOLD_YELLOW_UNDERLINE)
            print("1980 - 2023")

            genre = input("\nВведите жанр: ").lower()
            year = input("Введите год: ")
            movies, sql_query = search_movies_by_genre_and_year(genre, year)
            save_search_query(f"{genre} {year}", sql_query)
            display_movies(movies)

        elif choice == "3":
            queries = get_popular_search_queries()
            display_popular_queries(queries)

        elif choice == "4":
            print_formated("Выход из программы.", BOLD_RED)
            break

        else:
            print_formated("Неверный выбор. Пожалуйста, попробуйте снова.", BOLD_RED)

def display_movies(movies):
    if movies:
        print_formated(f"\nНайдено фильмов: {len(movies)}", BOLD_GREEN)
        for movie in movies:
            print(f'Название: "{movie.get("title")}"({movie.get("release_year")}). '
                  f'\n📝Описание фильма: {movie.get("description")}\n')
    else:
        print_formated("\nФильмы не найдены.", BOLD_RED)

def display_popular_queries(queries):
    if queries:
        print_formated("Самые популярные запросы (TOP 5):", BOLD_GREEN)
        for query in queries:
            print(f"Запрос: {query[0]}, Количество: {query[1]}")
    else:
        print_formated("\nПопулярные запросы не найдены.", BOLD_RED)

if __name__ == "__main__":
    main()
