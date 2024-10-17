from aiogram.fsm.state import StatesGroup, State


class CreateAccountClientState(StatesGroup):
    Name = State()
    Email = State()
    Amount = State()
    Timezone = State()

