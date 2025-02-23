###### Финальный проект по курсу Python Fundamentals
###### Дата защиты проекта: 28.02.2025

### ОПИСАНИЕ
Это консольное приложение для поиска фильмов в базе данных Sakila. 
Оно позволяет искать фильмы по ключевому слову, жанру и году, 
а также выводить самые популярные поисковые запросы.


### УСТАНОВКА
1. *Клонируйте репозиторий:*
    git clone https://github.com/ваш_пользователь/ваш_репозиторий.git
    cd ваш_репозиторий


2. *Создайте файл .env:*

Создайте файл .env в корневой директории проекта и добавьте туда данные 
для подключения к вашей базе данных MySQL:  

    HOST=localhost
    USER=ваш_пользователь
    PASSWORD=ваш_пароль
    DATABASE=sakila


3. *Установите зависимости:*

Убедитесь, что у вас установлен Python 3.x. Затем установите необходимые библиотеки:

    pip install pymysql
    pip install python-dotenv


4. *Запустите приложение:*
    
    python main.py
    


### ИСПОЛЬЗОВАНИЕ

После запуска приложения вы увидите меню с командами:

- Поиск фильмов по ключевому слову
- Поиск фильмов по жанру и году
- Показать популярные запросы
- Выйти

Следуйте инструкциям на экране, чтобы выполнить нужные действия.



### СТРУКТУРА ПРОЕКТА

- main.py                   # Основной файл для запуска приложения.
- config.py                 # Конфигурация и подключение к базе данных.
- sakila_queries.py         # SQL-запросы к БД sakila
- local_save_queries.py     # Функции для сохранения запросов и результатов в локальную БД sqlite3
- search_queries.db         # Локальная БД sqlite3 с результатами сохранения данных после выполнения программы
- .env                      # Файл с переменными окружения для подключения к базе данных.


###### Автор: Izzet Yunusov

### *Проект разработан в образовательных целях*