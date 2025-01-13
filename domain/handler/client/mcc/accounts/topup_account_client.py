import logging

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext
from colorama import Style

from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.transaction_rep.account_transaction import AccountTransactionRepository
from domain.notification.admin_notify import NotificationAdmin
from domain.states.client.account.TopUpAccountClientState import TopUpAccountClientState
from presentation.keyboards.client.kb_mcc.kb_accounts import TopUpClientAccount, kb_back_detail_account, \
    TopUpClientAccountConfirmation, kb_back_account_topup_confirmation

router = Router()


@router.callback_query(TopUpClientAccount.filter())
async def topup_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(TopUpAccountClientState.Value)
    await callback.message.edit_text(i18n.CLIENT.ACCOUNT.TOPUP.VALUE(), reply_markup=kb_back_detail_account)


@router.message(TopUpAccountClientState.Value)
async def topup_value_save(message: Message, state: FSMContext, i18n: I18nContext):
    try:
        topup_value = int(message.text)
        if topup_value < 100 or topup_value > 10000:
            raise ValueError
    except ValueError as e:
        await message.answer(i18n.CLIENT.MCC.BALANCE.VALUE.ERROR(), reply_markup=kb_back_detail_account)
        return

    data = await state.get_data()
    balance = BalanceRepository().balance(data['mcc_uuid'], data['team_uuid'])

    if balance['balance'] < topup_value:
        await message.answer(
            i18n.CLIENT.ACCOUNT.TOPUP.BALANCE.ERROR(balance=balance['balance'], value=topup_value),
            reply_markup=kb_back_detail_account
        )
        return

    await state.update_data(balance_uuid=balance['balance_uuid'])
    await state.update_data(team_name=balance['team_name'])
    await state.update_data(value=topup_value)
    await message.answer(i18n.CLIENT.ACCOUNT.TOPUP.WARNING(value=topup_value),
                         reply_markup=kb_back_account_topup_confirmation)


@router.callback_query(TopUpClientAccountConfirmation.filter(), TopUpAccountClientState.Value)
async def topup_account_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    await state.set_state(None)
    await callback.message.delete()

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(
            mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_detail_account
        )
        return

    resposne_trans = AccountTransactionRepository().topup_account_transaction_client(auth, data)

    if not resposne_trans['result']:
        logging.error(Style.BRIGHT + f"error topup by api {data['account_uid']}")
        await callback.message.answer(i18n.CLIENT.ACCOUNT.TOPUP.FAIL(), reply_markup=kb_back_detail_account)
        await NotificationAdmin.user_topup_account_error(callback.from_user.id, bot, i18n, data, resposne_trans['error'])
        return

    await callback.message.answer(i18n.CLIENT.ACCOUNT.TOPUP.SUCCESS(), reply_markup=kb_back_detail_account)
    await NotificationAdmin.user_topup_account(callback.from_user.id, bot, i18n, data)

