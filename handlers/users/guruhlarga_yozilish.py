import pickle
import types

from aiogram.types import Message,ReplyKeyboardRemove
from datetime import datetime
from data.config import ADMINS
from keyboards.default.startKeyboard import after_start_keyboard
from states.register_for_IT import Get_data
from aiogram.dispatcher.filters import Regexp
from keyboards.default.back import cansel_keyboard
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.misc import logging

numbers = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

@dp.message_handler(text_contains="Guruhlarga yozilish")
async def Register(message:Message):
    await message.answer("To'iq ismingizni kiritng:",reply_markup=ReplyKeyboardRemove())
    await Get_data.fullname.set()

@dp.message_handler(state=Get_data.fullname)
async def get_fullname(message:Message,state=FSMContext):
    name=message.text

    await state.update_data(
        {"name":name}
    )
    await message.answer("Telofon raqamizni kiriting:")
    await Get_data.next()

@dp.message_handler(Regexp(numbers),state=Get_data.number)
async def get_number(message:Message,state=FSMContext):
    number = message.text
    if number:
        await state.update_data(
            {"phone_num": number}
        )
        await message.answer("Qaysi dasturlash tilini bilasiz!!!")
        await Get_data.next()
    else:
        pass


@dp.message_handler(state=Get_data.language)
async def get_fullname(message:Message,state=FSMContext):
    language = message.text

    await state.update_data(
        {"language": language}
    )

    data = await state.get_data()
    name=data.get("name"),
    number=data.get("number"),
    language=data.get("language")

    msg1 = f"Yangi o'quvchi\n"
    msg = f"To'liq ismi -{name}\n"
    msg +=f"Telefon raqami -{number}\n"
    msg +=f"Dasturlash tili -{language}\n"

    # with open(f"{message.from_user.username}",'wb') as file:
    #     pickle.dump(datetime,file)
    #     pickle.dump(msg,file)


    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin,msg1)
            await dp.bot.send_message(admin,msg)

        except Exception as err:
            logging.exception(err)


    await message.answer("Rahmat qabul qilindi")
    await message.answer("Sizga operatorlarimiz bo'g'lanadi",reply_markup=cansel_keyboard)
    await state.finish()


@dp.message_handler(text="orqaga")
async def get_fullname(message:Message):
    await message.answer("Menu tanlang",reply_markup=after_start_keyboard)