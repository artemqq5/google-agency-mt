from aiogram.fsm.state import StatesGroup, State


class AddNewMCCState(StatesGroup):
    Name = State()
    Wallet = State()
    ID = State()
    SecretToken = State()
