# Запуск docker-compose проекта API_YAMDB
## Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Примененные технологии
+ Python 3.7
+ Django 2.2
+ DRF
+ JWT + Djoser
+ Postgresql
+ Docker
+ NGINX.

# Запуск проекта

### Docker-compose

- Создайте файл .env расположив его по пути ifra/.env
- Заполните файл .env по форме:
``` bash
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME= <..> # имя базы данных
POSTGRES_USER= <..> # логин для подключения к базе данных
POSTGRES_PASSWORD= <..> # пароль для подключения к БД
DB_HOST= <..> # название сервиса (контейнера)
DB_PORT= <..> # порт для подключения к БД 
```
### Запуск

- Переходим в папку с docker-compose:
```bash
cd infa
```
- Запустите контейнер:
```bash
docker-compose up -d --build 
```
- Выполните миграции:
```bash
docker-compose exec web python manage.py migrate
```
- Создайте суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```
- Соберите статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

# Документация
Документация будет доступна после запуска проекта по адресу /redoc/.

## Примеры некоторых запросов API
Регистрация пользователя:
```
POST /api/v1/auth/signup/
```
Получение данных своей учетной записи:
```
GET /api/v1/users/me/
```
Получение списка всех отзывов:
```
GET /api/v1/titles/{title_id}/reviews/
```
Добавление комментария к отзыву:
```
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Добавление новой категории:
```
POST /api/v1/categories/
```
Удаление жанра:
```
DELETE /api/v1/genres/{slug}
```
Частичное обновление информации о произведении:
```
PATCH /api/v1/titles/{titles_id}
```


Полный список запросов API находятся в документации.

### Автор
[Кузьмин Артём](https://github.com/MrKarlkarlsn) 

  
