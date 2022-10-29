from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

after_start_keyboard=ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Bizning kompaniya"),
        KeyboardButton("Guruhlarga yozilish"),
    ],
    [
        KeyboardButton("onlayn kurslar"),
        KeyboardButton("Ko'proq"),
    ],
    [
        KeyboardButton("IT school haqida")
    ],
],resize_keyboard=True)