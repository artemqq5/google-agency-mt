from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext, L

from data.constants import CLIENT
from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.taxes import TaxRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.filters.isTeamFilter import IsTeamFilter
from domain.handler.client.mcc import mcc_nav_client
from domain.handler.client.refunds import nav_refund
from domain.handler.client.taxes import nav_taxes
from domain.middlewares.IsUserRole import UserRoleMiddleware
from presentation.keyboards.client.kb_main_client import kb_menu_client
from presentation.keyboards.client.kb_mcc.kb_mcc import kb_client_mccs_manage
from presentation.keyboards.client.kb_refund.kb_refund import kb_client_refunds
from presentation.keyboards.client.kb_taxes.kb_taxes import kb_transaction_tax

router = Router()

router.include_routers(
    mcc_nav_client.router,
    nav_taxes.router,
    nav_refund.router
)

router.message.middleware(UserRoleMiddleware(CLIENT))
router.callback_query.middleware(UserRoleMiddleware(CLIENT))


@router.message(Command("start"), IsAdminFilter(False), IsTeamFilter(True))
async def start(message: Message, state: FSMContext, i18n: I18nContext):
    await state.clear()
    await message.answer(text=i18n.MENU(), reply_markup=kb_menu_client)


@router.message(F.text == L.CLIENT.ACCOUNTS(), IsTeamFilter(True))
async def accounts_manage(message: Message, i18n: I18nContext, state: FSMContext):
    # get access to get team_uuid and save it
    access = AccessRepository().access_by_user_id(message.from_user.id)
    await state.update_data(team_uuid=access['team_uuid'])

    # get available mcc for team by team_uuid
    mccs = MCCRepository().mccs_by_team_uuid(access['team_uuid'])
    await message.answer(text=i18n.CLIENT.MCC(), reply_markup=kb_client_mccs_manage(mccs))


@router.message(F.text == L.CLIENT.TAXES(), IsTeamFilter(True))
async def taxes_view(message: Message, i18n: I18nContext, state: FSMContext):
    # get access to get team_uuid and save it
    access = AccessRepository().access_by_user_id(message.from_user.id)
    await state.update_data(team_uuid=access['team_uuid'])

    transactions_tax = TaxRepository().taxes_by_team(access['team_uuid'])
    await message.answer(
        text=i18n.TEAMS.TRANSACTIONS.TAX(),
        reply_markup=kb_transaction_tax(transactions_tax, 1)
    )


@router.message(F.text == L.CLIENT.REFUND(), IsTeamFilter(True))
async def refunds_view(message: Message, i18n: I18nContext, state: FSMContext):
    # get access to get team_uuid and save it
    access = AccessRepository().access_by_user_id(message.from_user.id)
    await state.update_data(team_uuid=access['team_uuid'])

    refunded_accounts = SubAccountRepository().ref_accounts_by_team_uuid(access['team_uuid'])
    await message.answer(
        text=i18n.CLIENT.REFUND(),
        reply_markup=kb_client_refunds(refunded_accounts, 1)
    )
