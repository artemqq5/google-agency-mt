from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_teams.kb_teams import BackTeamManage


class TeamDeleteConfirmation(CallbackData, prefix="TeamDeleteConfirmation"):
    pass


kb_team_delete_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.DELETE(), callback_data=TeamDeleteConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=BackTeamManage().pack())],
])

