import math

from aiogram.filters.callback_data import CallbackData
from aiogram_i18n import L
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.keyboards.admin.kb_teams.kb_teams import TeamAccessesBack


# Delete Team Access
class DeleteTeamAccess(CallbackData, prefix="DeleteTeamAccess"):
    pass


kb_team_access_manage = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.ACCESS.DELETE(), callback_data=DeleteTeamAccess().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamAccessesBack().pack())],
])


# Delete Team Access Confirmation
class DeleteTeamAccessConfirmation(CallbackData, prefix="DeleteTeamAccessConfirmation"):
    pass


kb_team_access_delete_confirmation = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=L.TEAMS.ACCESS.DELETE.CONFIRMATION(), callback_data=DeleteTeamAccessConfirmation().pack())],
    [InlineKeyboardButton(text=L.BACK(), callback_data=TeamAccessesBack().pack())],
])


