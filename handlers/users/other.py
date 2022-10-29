from aiogram.types import Message
from loader import dp


@dp.message_handler(text_contains="Kitoblar")
async def view_books(message:Message):
    await message.answer("Kechirasiz kitoblar hali yuklanmadi!")

@dp.message_handler(text_contains="Porfolio")
async def view_books(message:Message):
    await message.answer("Kechirasiz Portfoliolar qo'yilmadi!")