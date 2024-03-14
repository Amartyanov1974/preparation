from environs import Env
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, Updater, CallbackQueryHandler

PAGE_SIZE = 3
PROGRAMMING_LANGUAGES = ['Python', 'Java', 'C', 'C++', 'JavaScript', 'TypeScript', 'Ruby', 'Swift', 'Go', 'PHP', 'Rust', 'Kotlin', 'Scala', 'Perl', 'Lua']
logger = logging.getLogger(__name__)

def get_page_keyboard(page):
    keyboard = []
    start_index = page * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    for i in range(start_index, min(end_index, len(PROGRAMMING_LANGUAGES))):
        keyboard.append([InlineKeyboardButton(PROGRAMMING_LANGUAGES[i], callback_data=str(i))])

    if start_index > 0:
        keyboard.append([InlineKeyboardButton('⬅️', callback_data=f'prev_{page}')])

    if end_index < len(PROGRAMMING_LANGUAGES):
        keyboard.append([InlineKeyboardButton('➡️', callback_data=f'next_{page}')])

    return keyboard

def start(update: Update, context: CallbackContext) -> None:
    keyboard = get_page_keyboard(0)
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = query.data

    if data.startswith('next_'):
        page = int(data.split('_')[1]) + 1
    elif data.startswith('prev_'):
        page = int(data.split('_')[1]) - 1
    else:
        query.edit_message_text(text=f"You selected {PROGRAMMING_LANGUAGES[int(data)]}")
        return

    keyboard = get_page_keyboard(page)
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Please choose:", reply_markup=reply_markup)

def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    env = Env()
    env.read_env()
    TG__BOT_TOKEN = env('TG__BOT_TOKEN')
    updater = Updater(TG__BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
