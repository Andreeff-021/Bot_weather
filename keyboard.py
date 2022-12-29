from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_hi = KeyboardButton('/start')

greet_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)