import logging

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext
from colorama import Style

from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.transaction_rep.account_transaction import AccountTransactionRepository
from domain.notification.admin_notify import NotificationAdmin
from presentation.keyboards.client.kb_mcc.kb_accounts import RefundClientAccount, RefundClientAccountConfirmation, \
    kb_back_account_refund_confirmation, kb_back_detail_account, kb_back_detail_mcc

router = Router()


@router.callback_query(RefundClientAccount.filter())
async def refund_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
    account = SubAccountRepository().account_by_uid(data['account_uid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.edit_text(
            i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_detail_account
        )
        return

    account_api_response = YeezyAPI().get_verify_account(auth['token'], data['account_uid'])
    account_api = account_api_response.get('accounts', [{}])[0]

    account_commission = round(account_api['balance'] - (account_api['balance'] * 0.96), 3)

    await callback.message.edit_text(
        i18n.CLIENT.ACCOUNT.REFUND.CONFIRMATION.WARNING(
            account_name=account['account_name'],
            balance=account_api.get('balance', 'no info '),
            commission=str(account_commission)
        ),
        reply_markup=kb_back_account_refund_confirmation
    )


@router.callback_query(RefundClientAccountConfirmation.filter())
async def refund_account_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.edit_text(i18n.MCC.AUTH.FAIL(
            mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_detail_account
        )
        return

    response_refund_trans = AccountTransactionRepository().refund_transaction_client(auth, data)
    if not response_refund_trans['result']:
        logging.error(Style.BRIGHT + f"error refund by api {data['account_uid']}")
        await callback.message.edit_text(i18n.CLIENT.ACCOUNT.REFUND.FAIL(), reply_markup=kb_back_detail_account)
        await NotificationAdmin.user_refund_account_error(callback.from_user.id, bot, i18n, data, data['account'], response_refund_trans['error'])
        return

    await callback.message.edit_text(i18n.CLIENT.ACCOUNT.REFUND.SUCCESS(), reply_markup=kb_back_detail_mcc)
    await NotificationAdmin.user_refund_account(callback.from_user.id, bot, i18n, data, data['account'])
