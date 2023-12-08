Данный проект представляет собой бэкенд-часть SPA веб-приложения.

## Используемые технологии

  * Язык: python (версия интерпретатора python - 3.11.)
  * Фреймфорк: django (Django REST framework)
  * БД (СУБД) проекта: PostgreSQL
  * python
  * drf-yasg
  * cors
  * jwt (simple jwt)


## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:
* http://127.0.0.1:8000/redoc/ - ссылка на редок
* http://127.0.0.1:8000/docs/ - ссылка на сваггер

## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 

В модуле ``settings.py`` необходимо внести изменения в следующие настройки, 
если у вас есть сторонние домены, обращающиеся к вашему API:

```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```

## Запуск проекта
* Склонировать репозиторий в IDE: 
   В терминале ввести команду: git clone https://github.com/violetta-p/DRF_Proj

* Установить виртуальное окружение и зависимости из файла requirements.txt:

  Ввести следующие команды в терминале:
  1. Создать виртуальное окружение: python3 -m venv venv
  2. Активировать виртуальное окружение: venv\Scripts\activate.bat (Windows), 
                                         source venv/bin/activate (Linux)
  3. Установить зависимости: pip install -r requirements.txt 
  4. Создать файл .env по шаблону из файла .env.sample

* Создать БД с названием, указанным в шаблоне (в пункте 4)

* Создать таблицы в БД. Создать миграции:
      python manage.py makemigrations
      python manage.py migrate

* Запустить сервер: python manage.py runserver

* Работа с docker:
  1. Создать образы: docker-compose build
  2. Запустить контейнеры: docker-compose up

* Настройка сервера:
    Установите необходимое ПО на сервере:
        sudo apt-get update
        sudo apt-get install postgresql postgresql-contrib python3-pip
    
* Создайте базу данных и пользователя PostgreSQL для вашего проекта:
        sudo -u postgres psql
        CREATE DATABASE yourdbname;
        CREATE USER yourdbuser WITH PASSWORD 'yourpassword';
        ALTER ROLE yourdbuser SET client_encoding TO 'utf8';
        ALTER ROLE yourdbuser SET default_transaction_isolation TO 'read committed';
        ALTER ROLE yourdbuser SET timezone TO 'UTC';
        GRANT ALL PRIVILEGES ON DATABASE yourdbname TO yourdbuser;

* Установите необходимые Python-пакеты на сервер с помощью pip:
        pip3 install virtualenv

* Скопируйте свой Django-проект на сервер (например, через git clone или через SCP).

###Автор проекта:
@Viit_115
