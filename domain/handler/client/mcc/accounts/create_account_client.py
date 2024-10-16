import logging
import re

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L
from colorama import Style

from presentation.keyboards.client.kb_mcc.kb_accounts import CreateSubAccountClient

router = Router()


@router.callback_query(CreateSubAccountClient.filter())
async def create_account(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    pass
