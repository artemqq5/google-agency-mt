from aiogram.fsm.state import StatesGroup, State


class ChangeEmailAccountClientState(StatesGroup):
    Email = State()
