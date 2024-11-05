import uuid

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.YeezyAPI import YeezyAPI
from data.constants import ADMIN
from data.repositories.accesses import AccessRepository
from data.repositories.mcc import MCCRepository
from data.repositories.teams import TeamRepository
from data.repositories.transactions import TransactionRepository
from domain.filters.isAdminFilter import IsAdminFilter
from domain.handler.admin.teams import create_team, delete_team
from domain.handler.admin.teams.access import nav_access
from domain.middlewares.IsUserRole import UserRoleMiddleware
from domain.states.admin.mcc.AddNewMCCState import AddNewMCCState
from presentation.keyboards.admin.kb_main_admin import kb_menu_admin
from presentation.keyboards.admin.kb_mcc.kb_mcc import *

router = Router()


@router.callback_query(AddNewMCC.filter())
async def add_mcc(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await state.set_state(AddNewMCCState.Name)
    await callback.message.edit_text(text=i18n.MCC.ADD.NAME(), reply_markup=kb_back_mccs)


@router.message(AddNewMCCState.Name)
async def save_mcc_name(message: Message, state: FSMContext, i18n: I18nContext):
    if len(message.text) >= 50:
        await message.answer(
            text=i18n.MCC.ADD.NAME_ERROR(symballs=len(message.text)),
            reply_markup=kb_back_mccs
        )
        return

    await state.update_data(mcc_name=message.text)
    await state.set_state(AddNewMCCState.Wallet)
    await message.answer(text=i18n.MCC.ADD.WALLET(), reply_markup=kb_back_mccs)


@router.message(AddNewMCCState.Wallet)
async def save_mcc_wallet(message: Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(wallet=message.text)
    await state.set_state(AddNewMCCState.ID)
    await message.answer(text=i18n.MCC.ADD.ID(), reply_markup=kb_back_mccs)


@router.message(AddNewMCCState.ID)
async def save_mcc_id(message: Message, state: FSMContext, i18n: I18nContext):
    await state.update_data(mcc_id=message.text)
    await state.set_state(AddNewMCCState.SecretToken)
    await message.answer(text=i18n.MCC.ADD.SECRET_TOKEN(), reply_markup=kb_back_mccs)


@router.message(AddNewMCCState.SecretToken)
async def save_mcc_secret_token(message: Message, state: FSMContext, i18n: I18nContext):

    data = await state.get_data()
    mcc_secret_token = message.text

    # generate UUID for MCC
    mcc_uuid = uuid.uuid4()

    await state.set_state(None)

    # Check with API
    if not YeezyAPI().generate_auth(mcc_id=data['mcc_id'], mcc_secret_token=mcc_secret_token):
        await message.answer(i18n.MCC.ADD.FAIL(error="Check MCC account API"), reply_markup=kb_back_mccs)
        return

    # create MCC in database
    if not MCCRepository().add(mcc_uuid, data['mcc_name'], data['mcc_id'], mcc_secret_token, data['wallet']):
        await message.answer(i18n.MCC.ADD.FAIL(error="Create Team DB"), reply_markup=kb_back_mccs)
        return

    await message.answer(text=i18n.MCC.ADD.SUCCESS(mcc_name=data['mcc_name']), reply_markup=kb_back_mccs)
