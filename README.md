# Подготовка к работе на проекте

### Библиотека HTTPX
Отправить GET запрос с JSON
Отправить POST запрос с JSON
```python
import httpx
from pprint import pprint


def get_example(data: dict) -> dict:
    answer = httpx.get('https://httpbin.org/get', params=data)
    answer.raise_for_status()
    return answer.json()


def post_example(data: dict) -> dict:
    answer = httpx.post('https://httpbin.org/post', data=data)
    answer.raise_for_status()
    return answer.json()


def main():
    data = {'ключ': 'значение'}
    try:
        pprint(get_example(data))
        pprint(post_example(data))
    except Exception as e:
        print('Ошибка: ', e)


if __name__ == '__main__':
    main()
```

### Библиотека Pydantic v1
Написать вложенную схему валидации данных, получить ошибки валидации<br>
Экспортировать данные в формат JSON с помощью Pydantic<br>
Прочитать данные из JSON с помощью Pydantic<br>
Написать вложенную схему валидации переменных окружения (настройки приложения), получить ошибки валидации<br>

### Документация Telegram Bot API
### Pytest
### Product Flow
### Библиотека Tg API
### Starter Pack / Local-окружение
### Starter Pack / Contrib Candidates / Yostate
### Starter Pack / Прикладной код
Добавить ещё хотя бы один стейт в бота -- вложенное меню с кнопками<br>
Добавить стейт с параметрами: вывести пагинированный список языков программирования<br>
Написать свой декоратор для роутера, чтобы при каждом переходе из состояния в состояние чат-бот сообщал пользователю в Telegram локатор нового состояния<br>
### GitLab Merge Requests
Создать Merge Request c любым изменением в коде Tg API<br>
Отменить MR<br>
