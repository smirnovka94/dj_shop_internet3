# Описание проекта
Проект серверного приложения интернет магазина
База данных - Postgres
БД представляет собой таблицы товаров и блог с описанием товаров:

1)Таблица товаров (Категория, Продукт, Версия продукта);

2)Таблица блога


### Хранятся модели по пути
dj_shop_internet3/main/models

# Запуск проекта

### скопировать репозиторий
```
git clone https://github.com/smirnovka94/dj_shop_internet3.git
```
### установить виртуальное окружение
```
python -m venv venv
```
### установить библиотеки
```
pip install -r src\requirements.txt
```
### создать базу данных в PgAdmin с именем <shop_internet3>

### создать файл <.env> из <.env.example>
В качестве примера можно использовать данные
CACHE_ENABLED=1
CACHE_LOCATION=redis://127.0.0.1:6379
CACHE_EMAIL_HOST_USER=fuchup@oscarbot.ru
CACHE_EMAIL_HOST_PASSWORD=AsTSNVv7pun9
### создаем миграции
```
python manage.py makemigrations
python manage.py migrate
```
### загружаем базу данных
```
python manage.py loaddata data.json    
```
### Запуcтить приложение
```
python manage.py runserver 
```
