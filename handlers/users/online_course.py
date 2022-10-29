from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove
from keyboards.inline.online_course import course
from keyboards.inline.callback_data import course_data

from loader import dp

@dp.message_handler(text_contains="onlayn kurslar")
async def enter_course(msg:Message):
    await msg.answer("Kurs tanlang",reply_markup=course)

@dp.callback_query_handler(course_data.filter(item_name="komp_course"))
async def online_course(call:CallbackQuery):
    await call.answer("Online Darslar hozircha yoq",show_alert=False)
    await call.answer(cache_time=50)


@dp.callback_query_handler(course_data.filter(item_name="python_course"))
async def online_course(call: CallbackQuery):
    await call.answer("Online Darslar hozircha yoq", show_alert=False)
    await call.answer(cache_time=50)


@dp.callback_query_handler(course_data.filter(item_name="grafik_course"))
async def online_course(call: CallbackQuery):
    await call.answer("Online Darslar hozircha yoq", show_alert=False)
    await call.answer(cache_time=50)


@dp.callback_query_handler(course_data.filter(item_name="web_course"))
async def online_course(call: CallbackQuery):
    await call.answer("Online Darslar hozircha yoq", show_alert=False)
    await call.answer(cache_time=50)


@dp.callback_query_handler(course_data.filter(item_name="Android_course"))
async def online_course(call: CallbackQuery):
    await call.answer("Online Darslar hozircha yoq", show_alert=False)
    await call.answer(cache_time=50)


@dp.callback_query_handler(course_data.filter(item_name="robot_course"))
async def online_course(call: CallbackQuery):
    await call.answer("Online Darslar hozircha yoq", show_alert=False)
    await call.answer(cache_time=50)

@dp.callback_query_handler(course_data.filter(item_name="cancel"))
async def online_course(call: CallbackQuery):
    await call.message.delete()

