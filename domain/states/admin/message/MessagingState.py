from aiogram.fsm.state import StatesGroup, State


class MessagingState(StatesGroup):
    Message = State()
    Image = State()
