from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from domain.handler.admin.specific import load_accounts
from presentation.keyboards.admin.kb_specific.kb_specific import SpecificMain, kb_specific_main

router = Router()

router.include_routers(
    load_accounts.router
)


@router.callback_query(SpecificMain.filter())
async def main_specific(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.answer(i18n.ADMIN.SPECIFIC(), reply_markup=kb_specific_main)

