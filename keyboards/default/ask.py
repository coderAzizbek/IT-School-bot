from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ask_Person = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("🧑🏻‍💻 Ishga kirish"),
        KeyboardButton(" 🛍 Buyurtma berish"),
    ],
    [
        KeyboardButton("Virtual group haqida")
    ],
    [
        KeyboardButton("Bosh Menu"),
    ]

],resize_keyboard=True)

Homepage=ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Bosh Menu"),
    ]
],resize_keyboard=True)
    