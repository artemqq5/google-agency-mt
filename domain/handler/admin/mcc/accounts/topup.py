import logging

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L
from colorama import Style

from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from domain.states.admin.account.TopUpAccountState import TopUpAccountState
from presentation.keyboards.admin.kb_mcc.kb_accounts import TopUpAccount, kb_back_account, \
    kb_account_topup_confirmation, TopUpAccountConfirmation

router = Router()


@router.callback_query(TopUpAccount.filter())
async def topup_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TopUpAccountState.Value)
    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.TOPUP.VALUE(), reply_markup=kb_back_account)


@router.message(TopUpAccountState.Value)
async def topup_value_save(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        topup_value = int(message.text)
        if topup_value < 50 or topup_value > 10000:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.ADMIN.MCC.BALANCE.VALUE.ERROR(), reply_markup=kb_back_account)
        return

    await state.update_data(value=topup_value)
    await message.answer(i18n.ADMIN.ACCOUNT.TOPUP.WARNING(value=topup_value), reply_markup=kb_account_topup_confirmation)


@router.callback_query(TopUpAccountConfirmation.filter())
async def topup_account_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.edit_text(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    if not YeezyAPI().topup(auth['token'], data['account_uid'], data['value']):
        logging.error(Style.BRIGHT + f"error topup by api {data['account_uid']}")
        await callback.message.edit_text(i18n.ADMIN.ACCOUNT.TOPUP.FAIL(), reply_markup=kb_back_account)
        return

    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.TOPUP.SUCCESS(), reply_markup=kb_back_account)


