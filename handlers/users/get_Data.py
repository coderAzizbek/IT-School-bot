import logging
import pickle
from aiogram import types
from datetime import datetime
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, KeyboardButton
from keyboards.default.contactKeyboard import contact
from keyboards.default.startKeyboard import after_start_keyboard
from states.registration import PersonalData
from loader import dp
from keyboards.default.ask import ask_Person
from keyboards.default.get_data import know_Person
from aiogram.dispatcher import FSMContext
from keyboards.default.back import back_keyboard
from aiogram.dispatcher.filters import Regexp
from data.config import ADMINS

number = '^[0-9]{1,9}$'
phone_number="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


@dp.message_handler(text="Bizning kompaniya")
async def view_company(message: Message):
    await message.answer("Bizning kampaniya", reply_markup=ask_Person)


@dp.message_handler(text_contains="Ishga kirish")
async def view_button(message: Message):
    await message.answer("Sizni ishga olishimiz uchun ro'yhatdan o'tishiz kerak 🫡", reply_markup=know_Person)


@dp.message_handler(text_contains="Ro'yxatdan o'tish")
async def register_person(message: Message):
    await message.answer("To'iq ismingizni kiritng\nmasalan (Jumaboyev Jumavoy)", reply_markup=ReplyKeyboardRemove())
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def get_fullname(message: types.Message, state=FSMContext):
    name = message.text
    await state.update_data(

        {"fullname": name}
    )

    await message.answer("Yoshiz nechida")
    await PersonalData.next()


@dp.message_handler(Regexp(number), state=PersonalData.Age)
async def get_fullname(message: types.Message, state=FSMContext):
    age = len(message.text)
    if age == 3 or age > 3:
        await message.reply("Iltimos to'g'ri malumot kiriting")

    else:
        age = message.text
        await state.update_data(
            {"age": age}
        )

        await message.answer("Bizga telefon raqamizni yuboring ")
        await PersonalData.next()


@dp.message_handler(Regexp(phone_number), state=PersonalData.cantact)
async def get_lan(message: types.Message,state=FSMContext):
    phone_num = message.text
    if phone_num:
        await state.update_data(
            {"phone_num": phone_num}
        )
        await message.answer("Qaysi dasturlash tilini bilasiz!!!")
        await PersonalData.next()
    else:
        pass



    # await message.answer("Rahmat qabul qilindi", reply_markup=ReplyKeyboardRemove())
    # bot.delete_message(chat_id=message.from_user.id,message_id=message_id)




@dp.message_handler(state=PersonalData.language)
async def get_lan(message: types.Message, state=FSMContext):
    lan = message.text
    await state.update_data(
        {"lan": lan}
    )

    await message.answer("Biz sizni qilgan ishlaringizni ko'rishimiz uchun \n<code>GitHub</code> accountizni "
                         "yuboring.Iltimos faqat to'gri malumot yuboring!!!")
    await PersonalData.next()

@dp.message_handler(text="Malumotnoma")
@dp.message_handler(state=PersonalData.github)
async def get_github(message: types.Message, state=FSMContext):
    github = message.text
    await state.update_data(
        {"github": github}
    )

    # message_id = (await message.answer("Rahmat qabul qilindi")).message_id
    # bot.delete_message(chat_id=message.from_user.id, message_id=message_id)

    # Olingan malumotlar

    data = await state.get_data()
    fullname2 = data.get("fullname")
    age2 = data.get("age")
    phone_num2 = data.get("phone_num")
    lan2 = data.get("lan")
    github2 = data.get("github")

    xabar="Yangi malumot olindi"
    msg = f"To'liq ism - {fullname2}\n"
    msg += f"Yosh - {age2}\n"
    msg += f"telefon raqam - {phone_num2}\n"
    msg += f"Dasturlash til- {lan2}\n"
    msg += f"GitHub account: - <code>{github2}</code>"

    with open(f"{message.from_user.username}","w") as file:
        file.write("Sizning malumotnomangiz:\n")
        file.write(f"{msg}\n")

    await message.answer("Biz sizga bog'lanamiz", reply_markup=back_keyboard)
    await state.finish()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin,xabar)
            await dp.bot.send_message(admin,msg)

        except Exception as err:
            logging.exception(err)

@dp.message_handler(text_contains="Malumotnoma")
async def student_info(message:Message):
    with open(f"{message.from_user.username}",'r') as file:
        # student = file.read()
        await message.answer(file.read())

@dp.message_handler(text="Orqaga")
async def cansel(message:Message):
    await message.answer("Menu tanlang",reply_markup=ask_Person)

@dp.message_handler(text="Bosh Menu")
async def Main_menu(message:Message):
    await message.answer("Bosh menu",reply_markup=after_start_keyboard)