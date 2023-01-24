# Api_Yatube
![python version](https://img.shields.io/badge/Python-3.17-green)
![django version](https://img.shields.io/badge/Django-2.3-green)
![pillow version](https://img.shields.io/badge/Pillow-8.3-green)
![pytest version](https://img.shields.io/badge/pytest-6.2-green)
![PyJWT version](https://img.shields.io/badge/PyJWT-2.1-green)
![sorl-thumbnail version](https://img.shields.io/badge/djangorestframework-3.12-green)


## Описание проекта 
Api для проекта Yatube https://github.com/Not-user-1984/hw05_final.
Реализован API для всех моделей приложения. По запросу можно просмотреть все записи автора.
Пользователи могут делать запросы к чужим страницам, комментировать записи различных авторов, подписываться на них.
API доступен только аутентифицированным пользователям. Реализованы возможность поиска и фильтрации данных.
Добавлена пагинация ответов. Модели написаны с использованием вьюсетов. 
Подробная документация   http://127.0.0.1:8000/redoc/ после запуска проекта.

# Используемые технологии

Python 3.9, Django 2.2 LTS, Django ORM, Django REST Framework (DRF), REST API, SQLite3, CSRF, Paginator, Simple-JWT, Djoser

## Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Not-user-1984/api_final_yatube.git
```
```
cd api_final_yatube
```
- Cоздать и активировать виртуальное окружение:
```
py -m venv venv
```
```
source venv/scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```

## Настроены такие эндпоинты:

```
    api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
    api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
    api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
    api/v1/groups/ (GET): получаем список всех групп.
    api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
    api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или 
    создаём новый, указав id поста, который хотим прокомментировать.
    api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или 
    удаляем комментарий по id у поста с id=post_id.
```
## Примеры запросов:

```
- Пример POST-запроса с токеном Антона Чехова: добавление нового поста.
POST .../api/v1/posts/
```
- Пример ответа:
```
{
    "text": "некий текст поста",
    "group": 1
} 
```
- Пример GET-запроса: получаем информацию о группе.
GET .../api/v1/groups/2/

- Пример ответа:
```
{
    "id": 2,
    "title": "Кот",
    "slug":'cat",
    "description": "Посты на тему котов"
} 
```
# Разработчик

[ Дима Плужников ](https://github.com/Not-user-1984)
