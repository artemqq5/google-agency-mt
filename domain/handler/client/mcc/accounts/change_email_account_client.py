import logging
import re

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L
from colorama import Style

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from domain.notification.admin_notify import NotificationAdmin
from domain.states.client.account.ChangeEmailAccountClientState import ChangeEmailAccountClientState
from presentation.keyboards.client.kb_mcc.kb_accounts import ChangeEmailClientAccount, kb_back_detail_account

router = Router()


@router.callback_query(ChangeEmailClientAccount.filter())
async def change_email_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ChangeEmailAccountClientState.Email)
    await callback.message.edit_text(i18n.CLIENT.ACCOUNT.CHANGE_EMAIL(), reply_markup=kb_back_detail_account)


def is_valid_email(email: str) -> bool:
    # Регулярний вираз для валідації email-адреси
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Перевірка, чи відповідає email регулярному виразу
    if re.match(pattern, email):
        return True
    else:
        return False


@router.message(ChangeEmailAccountClientState.Email)
async def change_email_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    new_email = message.text
    if not is_valid_email(new_email):
        await message.answer(i18n.CLIENT.ACCOUNT.CHANGE_EMAIL.ERROR(), reply_markup=kb_back_detail_account)
        return

    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    change_email_result = YeezyAPI().change_email(auth['token'], data['account_uid'], new_email)

    if not change_email_result:
        logging.error(Style.BRIGHT + "error chgange email by api")
        await message.answer(i18n.CLIENT.ACCOUNT.CHANGE_EMAIL.FAIL(), reply_markup=kb_back_detail_account)
        return

    if not SubAccountRepository().update_email_by_uid(new_email, data['account_uid']):
        logging.error(Style.BRIGHT + "error chgange email by database")
        await message.answer(i18n.CLIENT.ACCOUNT.CHANGE_EMAIL.FAIL(), reply_markup=kb_back_detail_account)
        return

    await message.answer(i18n.CLIENT.ACCOUNT.CHANGE_EMAIL.SUCCESS(email=new_email), reply_markup=kb_back_detail_account)
    await NotificationAdmin.user_change_email(message.from_user.id, bot, i18n, data)

