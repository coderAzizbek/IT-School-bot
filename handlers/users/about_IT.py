from aiogram.types import Message
from keyboards.default.startKeyboard import after_start_keyboard
from keyboards.default.back import cansel_keyboard
from loader import dp

@dp.message_handler(text_contains="IT school haqida")
async def it_about(message:Message):
    await message.answer("Uzur IT school haqida malumot hali qo'yilmadi",reply_markup=cansel_keyboard)

@dp.message_handler(text="orqaga")
async def cansel(message:Message):
    await message.answer("Menu tanlang",reply_markup=after_start_keyboard)

