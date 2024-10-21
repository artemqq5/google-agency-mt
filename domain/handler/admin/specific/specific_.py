from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.handler.admin.specific import load_accounts
from presentation.keyboards.admin.kb_specific.kb_specific import kb_specific_main, SpecificMainBack

router = Router()

router.include_routers(
    load_accounts.router
)


@router.callback_query(SpecificMainBack.filter())
async def main_specific_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(i18n.ADMIN.SPECIFIC(), reply_markup=kb_specific_main)

