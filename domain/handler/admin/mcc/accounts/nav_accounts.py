from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from domain.handler.admin.mcc.accounts import change_team, change_email, topup, refund
from presentation.keyboards.admin.kb_mcc.kb_accounts import *

router = Router()

router.include_routers(
    change_team.router,
    change_email.router,
    topup.router,
    refund.router
)


@router.callback_query(BackAccountsManage.filter())
async def accounts_back(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    data = await state.get_data()

    mcc = MCCRepository().mcc_by_uuid(data['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get master balance with Auth Token MCC
    mcc_balance = YeezyAPI().get_master_balance(auth['token'])

    # Get Accounts From DataBase
    accounts = SubAccountRepository().accounts_by_mcc_uuid(data['mcc_uuid'])
    status = '✅' if bool(mcc['is_general']) else '❌'

    await callback.message.edit_text(
        text=i18n.MCC.DETAIL(
            name=mcc['mcc_name'],
            balance=mcc_balance.get('balances', {}).get('USD', 'Error. No USD balance '),
            general=status
        ),
        reply_markup=kb_accounts_manage(accounts, data['mcc_uuid'],
                                        data.get(
                                            'last_page_accounts',
                                            1)))


@router.callback_query(NavigationAccount.filter())
async def accounts_nav(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()

    accounts = SubAccountRepository().accounts_by_mcc_uuid(data['mcc_uuid'])

    await state.update_data(last_page_accounts=page)

    await callback.message.edit_reply_markup(reply_markup=kb_accounts_manage(accounts, data['mcc_uuid'], page))


@router.callback_query(ShowDetailAccount.filter())
async def account_detail(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    account_uid = callback.data.split(":")[1]
    account = SubAccountRepository().account_by_uid(account_uid)
    mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get Account API info
    account_api_response = YeezyAPI().get_verify_account(auth['token'], account_uid)
    if not account_api_response:
        await callback.answer(i18n.ADMIN.ACCOUNT.NO_VERIFY_YET(), show_alert=True)
        return

    account_api = account_api_response.get('accounts', [{}])[0]

    await state.update_data(account_uid=account_uid)

    await callback.message.edit_text(
        text=i18n.ACCOUNTS.DETAIL(
            name=account['account_name'],
            mcc_name=mcc['mcc_name'],
            status=account_api.get('status', 'no info'),
            email=account['account_email'],
            timezone=account['account_timezone'],
            customer_id=account_api.get('customer_id', 'no info'),
            balance=account_api.get('balance', 'no info '),
            spend=account_api.get('spend', 'no info '),
            limit=account_api.get('limit', 'no info '),
            team_name=account['team_name']
        ),
        reply_markup=kb_back_accounts
    )


@router.callback_query(ShowDetailAccountBack.filter())
async def account_detail_back(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
    data = await state.get_data()
    account = SubAccountRepository().account_by_uid(data['account_uid'])
    mcc = MCCRepository().mcc_by_uuid(account['mcc_uuid'])

    # Try Authorizate MCC API
    auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

    if not auth:
        await callback.message.answer(i18n.MCC.AUTH.FAIL(mcc_name=mcc['mcc_name']))
        return

    # Get Account API info
    account_api_response = YeezyAPI().get_verify_account(auth['token'], data['account_uid'])
    if not account_api_response:
        await callback.answer(i18n.ADMIN.ACCOUNT.NO_VERIFY_YET(), show_alert=True)
        return

    account_api = account_api_response.get('accounts', [{}])[0]

    await callback.message.edit_text(
        text=i18n.ACCOUNTS.DETAIL(
            name=account['account_name'],
            mcc_name=mcc['mcc_name'],
            status=account_api.get('status', 'no info'),
            email=account['account_email'],
            timezone=account['account_timezone'],
            customer_id=account_api.get('customer_id', 'no info'),
            balance=account_api.get('balance', 'no info '),
            spend=account_api.get('spend', 'no info '),
            limit=account_api.get('limit', 'no info '),
            team_name=account['team_name']
        ),
        reply_markup=kb_back_accounts
    )
