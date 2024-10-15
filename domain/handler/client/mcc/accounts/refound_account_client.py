from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from presentation.keyboards.client.kb_mcc.kb_accounts import RefoundClientAccount

router = Router()


@router.callback_query(RefoundClientAccount.filter())
async def refound_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    pass
