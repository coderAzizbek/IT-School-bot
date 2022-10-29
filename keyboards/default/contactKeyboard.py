from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

contact=ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Contact yuborish",request_contact=True)
    ],
],resize_keyboard=True)