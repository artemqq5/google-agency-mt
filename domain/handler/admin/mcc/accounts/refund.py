import logging

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext
from colorama import Style

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from presentation.keyboards.admin.kb_mcc.kb_accounts import RefundAccount, kb_back_account, \
    kb_account_refund_confirmation, RefundAccountConfirmation

router = Router()


@router.callback_query(RefundAccount.filter())
async def refund_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])
    account = SubAccountRepository().account_by_uid(data['account_uid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.edit_text(
            i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_account
        )
        return

    account_api_response = YeezyAPI().get_verify_account(auth['token'], data['account_uid'])
    account_api = account_api_response.get('accounts', [{}])[0]

    await callback.message.edit_text(
        i18n.ADMIN.ACCOUNT.REFUND.CONFIRMATION.WARNING(
            account_name=account['account_name'],
            balance=account_api.get('balance', 'no info ')
        ),
        reply_markup=kb_account_refund_confirmation
    )


@router.callback_query(RefundAccountConfirmation.filter())
async def refund_account_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    data = await state.get_data()
    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.edit_text(i18n.MCC.AUTH.FAIL(
            mcc_name=mcc['mcc_name']),
            reply_markup=kb_back_account
        )
        return

    if not YeezyAPI().refund(auth['token'], data['account_uid']):
        logging.error(Style.BRIGHT + f"error refund by api {data['account_uid']}")
        await callback.message.edit_text(i18n.ADMIN.ACCOUNT.REFUND.FAIL(), reply_markup=kb_back_account)
        return

    await callback.message.edit_text(i18n.ADMIN.ACCOUNT.REFUND.SUCCESS(), reply_markup=kb_back_account)
