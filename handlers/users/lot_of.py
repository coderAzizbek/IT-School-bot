from aiogram.types import Message
from keyboards.default.a_lot_of import lot_of
from keyboards.default.startKeyboard import after_start_keyboard
from loader import dp

@dp.message_handler(text_contains="Ko'proq")
async def view_lot_of(message:Message):
    await message.answer('Menu tanlang',reply_markup=lot_of)

@dp.message_handler(text="orqaga")
async def get_fullname(message:Message):
    await message.answer("Menu tanlang",reply_markup=after_start_keyboard)