import os

from environs import Env
from tg_api import (
    SyncTgClient,
    SendMessageRequest,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    SendUrlPhotoRequest,
    SendBytesPhotoRequest,
    )


def send_button(telegram_token, telegram_chat_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Кнопка1', callback_data='action1'),
                InlineKeyboardButton(text='Кнопка2', callback_data='action2'),
            ],
        ],
    )

    with SyncTgClient.setup(telegram_token):
        tg_request = SendMessageRequest(
            chat_id=telegram_chat_id,
            text='Кнопки',
            reply_markup=keyboard,
        )
        tg_request.send()


def send_response_template(telegram_token, telegram_chat_id):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Ответ1'),
                KeyboardButton(text='Ответ2'),
            ],
        ],
        resize_keyboard=True
    )

    with SyncTgClient.setup(telegram_token):
        tg_request = SendMessageRequest(
            chat_id=telegram_chat_id,
            text='Шаблоны ответа',
            reply_markup=keyboard,
        )
        tg_request.send()


def send_url_photo(
    telegram_token,
    telegram_chat_id,
    photo_url,
    photo_filename='Фото книги'):

    with SyncTgClient.setup(telegram_token):
        tg_request = SendUrlPhotoRequest(
            chat_id=telegram_chat_id,
            caption=photo_filename,
            photo=photo_url,
            filename=photo_filename,
        )
        tg_request.send()


def send_photo(
    telegram_token,
    telegram_chat_id,
    photo_dir,
    photo_name):
    photo_path = os.path.join(photo_dir, photo_name)
    with SyncTgClient.setup(telegram_token):
        with open(photo_path, 'rb') as photo_file:
            photo = photo_file.read()
        tg_request = SendBytesPhotoRequest(
            chat_id=telegram_chat_id,
            photo=photo,
            caption='Фото книги',
            filename=photo_name,
        )
        tg_request.send()


def main():
    env = Env()
    env.read_env()
    telegram_token = env('TELEGRAM_TOKEN')
    telegram_chat_id = env('TELEGRAM_CHAT_ID')

    photo_dir = './photo'
    photo_name = '18919.jpg'
    send_photo(telegram_token, telegram_chat_id, photo_dir, photo_name)

    photo_url = 'https://amartyanov1974.github.io/online_library/media/images/13038.jpg'
    send_url_photo(telegram_token, telegram_chat_id, photo_url)

    send_button(telegram_token, telegram_chat_id)

    send_response_template(telegram_token, telegram_chat_id)


if __name__ == '__main__':
    main()
