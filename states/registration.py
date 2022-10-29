from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    fullname = State()
    Age = State()
    cantact = State()
    language = State()
    github = State()
