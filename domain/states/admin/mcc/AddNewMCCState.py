from aiogram.fsm.state import StatesGroup, State


class AddNewMCCState(StatesGroup):
    Name = State()
    ID = State()
    SecretToken = State()
