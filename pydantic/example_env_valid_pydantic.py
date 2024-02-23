import re
import json

from environs import Env
from pydantic import BaseModel, validator


class User(BaseModel):
    latin_text: str
    cyril_text: str
    email: str
    """
    Вложенная схема валидации данных
    """
    @validator('latin_text')
    def validate_latin_text(cls, value):
        if not bool(re.fullmatch(r'[a-zA-Z]+', value)):
            raise ValueError('latin_text is invalid')
        return value

    @validator('cyril_text')
    def validate_cyril_text(cls, value):
        if not bool(re.fullmatch(r'[а-яА-ЯёЁ]+', value)):
            raise ValueError('cyril_text is invalid')
        return value

    @validator('email')
    def validate_email(cls, value):
        if not bool(re.fullmatch(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+', value)):
            raise ValueError('Email is invalid')
        return value


def main():
    env = Env()
    env.read_env()
    """
    В файле .env содержатся следующие переменные среды:

    LATIN_TEXT_VAL=qwertyuiop
    CYRIL_TEXT_VAL=йцукенгшфывапр
    EMAIL_VAL=to.email@email.com
    LATIN_TEXT_INVAL=qwertyuiopй
    CYRIL_TEXT_INVAL=йцукенгшфывапрz
    EMAIL_INVAL=to.email-email.com

    """
    latin_text = env('LATIN_TEXT_VAL')
    cyril_text = env('CYRIL_TEXT_VAL')
    email = env('EMAIL_VAL')

    user_values = {
        'latin_text': 'LatinText',
        'cyril_text': 'ТекстКирилицей',
        'email': 'new.mail@mail.com',
        }
    user_values = json.dumps(user_values, indent=4, ensure_ascii=False)
    # Прочитать данные из JSON с помощью Pydantic
    valid_result = User.parse_raw(user_values)
    print(valid_result.json(indent=4, ensure_ascii=False))

    """
    Вывод:
    {
        "latin_text": "LatinText",
        "cyril_text": "ТекстКирилицей",
        "email": "new.mail@mail.com"
    }
    """

    try:
        valid_result = User(
            latin_text=latin_text,
            cyril_text=cyril_text,
            email=email,
            )
        # Экспортировать данные в формат JSON с помощью Pydantic
        print(valid_result.json(indent=4, ensure_ascii=False))
        """
        Вывод:
        {
            "latin_text": "qwertyuiop",
            "cyril_text": "йцукенгшфывапр",
            "email": "to.email@email.com"
        }
        """

        latin_text = env('LATIN_TEXT_INVAL')
        cyril_text = env('CYRIL_TEXT_INVAL')
        email = env('EMAIL_INVAL')

        invalid_result = User(
            latin_text=latin_text,
            cyril_text=cyril_text,
            email=email,
            )
        print(invalid_result.json())

    except ValueError as e:
        print(json.dumps(e.errors(), ensure_ascii=False, indent=4))
        """
        Вывод:
        [
            {
                "loc": [
                    "latin_text"
                ],
                "msg": "latin_text is invalid",
                "type": "value_error"
            },
            {
                "loc": [
                    "cyril_text"
                ],
                "msg": "cyril_text is invalid",
                "type": "value_error"
            },
            {
                "loc": [
                    "email"
                ],
                "msg": "Email is invalid",
                "type": "value_error"
            }
        ]
        """


if __name__ == '__main__':
    main()
