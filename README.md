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

### создать файл <.env> из <.env.template>

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
