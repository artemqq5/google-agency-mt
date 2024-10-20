from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from domain.handler.client.mcc.accounts import change_email_account_client, \
    topup_account_client, create_account_client, refund_account_client
from domain.middlewares.AccessClientMCC import AccessClientMCCMiddleware
from presentation.keyboards.client.kb_mcc.kb_accounts import NavigationAccountClient, \
    ShowDetailAccountClient, kb_back_accounts_client, kb_accounts_manage_client, ShowDetailAccountClientBack

router = Router()

router.include_routers(
    change_email_account_client.router,
    refund_account_client.router,
    topup_account_client.router,
    create_account_client.router
)

router.message.middleware(AccessClientMCCMiddleware())
router.callback_query.middleware(AccessClientMCCMiddleware())


@router.callback_query(NavigationAccountClient.filter())
async def accounts_nav_client(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    page = int(callback.data.split(":")[1])
    data = await state.get_data()

    accounts = SubAccountRepository().accounts_by_team_uuid(data['mcc_uuid'], data['team_uuid'])

    await state.update_data(last_page_accounts=page)

    await callback.message.edit_reply_markup(reply_markup=kb_accounts_manage_client(accounts, page))


@router.callback_query(ShowDetailAccountClient.filter())
async def account_detail_client(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
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
        await callback.answer(i18n.CLIENT.ACCOUNT.NO_VERIFY_YET(), show_alert=True)
        return

    account_api = account_api_response.get('accounts', [{}])[0]

    await state.update_data(account_uid=account_uid)

    await callback.message.edit_text(
        text=i18n.CLIENT.ACCOUNTS.DETAIL(
            name=account['account_name'],
            mcc_name=mcc['mcc_name'],
            status=account_api.get('status', 'no info'),
            email=account['account_email'],
            timezone=account['account_timezone'],
            customer_id=account_api.get('customer_id', 'no info'),
            balance=account_api.get('balance', 'no info '),
            spend=account_api.get('spend', 'no info '),
            limit=account_api.get('limit', 'no info '),
        ),
        reply_markup=kb_back_accounts_client
    )


@router.callback_query(ShowDetailAccountClientBack.filter())
async def account_detail_client_back(callback: CallbackQuery, i18n: I18nContext, state: FSMContext):
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
    account_api = account_api_response.get('accounts', [{}])[0]

    await callback.message.edit_text(
        text=i18n.CLIENT.ACCOUNTS.DETAIL(
            name=account['account_name'],
            mcc_name=mcc['mcc_name'],
            status=account_api.get('status', 'no info'),
            email=account['account_email'],
            timezone=account['account_timezone'],
            customer_id=account_api.get('customer_id', 'no info'),
            balance=account_api.get('balance', 'no info '),
            spend=account_api.get('spend', 'no info '),
            limit=account_api.get('limit', 'no info '),
        ),
        reply_markup=kb_back_accounts_client
    )