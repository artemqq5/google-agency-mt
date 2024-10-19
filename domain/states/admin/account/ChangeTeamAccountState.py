from aiogram.fsm.state import StatesGroup, State


class ChangeTeamAccountState(StatesGroup):
    TeamUUID = State()
