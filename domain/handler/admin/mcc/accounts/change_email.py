import logging

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext
from colorama import Style

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from domain.states.admin.account.ChangeEmailAccountState import ChangeEmailAccountState
from presentation.keyboards.admin.kb_mcc.kb_accounts import ChangeEmailAccount, kb_back_account

router = Router()


@router.callback_query(ChangeEmailAccount.filter())
async def change_email_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(ChangeEmailAccountState.Email)
    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.CHANGE_EMAIL(), reply_markup=kb_back_account)


@router.message(ChangeEmailAccountState.Email)
async def change_email_save(message: Message, state: FSMContext, i18n: I18nContext, bot: Bot):
    new_email = message.text
    from domain.handler.client.mcc.accounts.change_email_account_client import is_valid_email
    if not is_valid_email(new_email):
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_EMAIL.ERROR(), reply_markup=kb_back_account)
        return

    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    if not SubAccountRepository().update_email_by_uid(new_email, data['account_uid']):
        logging.error(Style.BRIGHT + f"error chgange email by database {data['account_uid']} | {new_email}")
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_EMAIL.FAIL(), reply_markup=kb_back_account)
        return

    if not YeezyAPI().change_email(auth['token'], data['account_uid'], new_email):
        logging.error(Style.BRIGHT + f"error chgange email by api {data['account_uid']} | {new_email}")
        await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_EMAIL.FAIL(), reply_markup=kb_back_account)
        return

    await message.answer(i18n.ADMIN.ACCOUNT.CHANGE_EMAIL.SUCCESS(email=new_email), reply_markup=kb_back_account)
