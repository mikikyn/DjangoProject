from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --------------------------------------------------------------------
start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

start_buttons = KeyboardButton('/start')
info = KeyboardButton('/info')


start.add(start_buttons, info)

# --------------------------------------------------------------------
start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
    KeyboardButton('/start')
)

# --------------------------------------------------------------------

cancel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))