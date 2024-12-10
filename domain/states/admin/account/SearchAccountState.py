from aiogram.fsm.state import StatesGroup, State


class SearchAccountState(StatesGroup):
    email = State()

