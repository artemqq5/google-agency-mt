from aiogram.fsm.state import StatesGroup, State


class CreateAccountAdminState(StatesGroup):
    Name = State()
    TeamUUID = State()
    Email = State()
    Amount = State()
    Timezone = State()
