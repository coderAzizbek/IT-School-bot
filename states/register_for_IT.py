from aiogram.dispatcher.filters.state import StatesGroup, State


class Get_data(StatesGroup):
    fullname = State()
    number = State()
    language = State()

