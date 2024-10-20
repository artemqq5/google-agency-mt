from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext, L

from data.YeezyAPI import YeezyAPI
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from presentation.keyboards.admin.kb_specific.kb_specific import kb_specific_back, kb_load_account_confirmation, \
    SpecificLoadAccounts, SpecificLoadAccountsConfirmation

router = Router()


@router.callback_query(SpecificLoadAccounts.filter())
async def load_accounts_warning(callback: CallbackQuery, state: FSMContext, i18n: I18nContext):
    await callback.message.edit_text(i18n.ADMIN.SPECIFIC.LOAD.WARNING(), reply_markup=kb_load_account_confirmation)


@router.callback_query(SpecificLoadAccountsConfirmation.filter())
async def load_accounts_confirmation(callback: CallbackQuery, state: FSMContext, i18n: I18nContext, bot: Bot):
    mccs = MCCRepository().mccs()

    all_accounts = 0
    result = ""

    part_mcc = 0

    await callback.message.delete()
    await callback.message.answer(i18n.ADMIN.SPECIFIC.LOAD.PROCESSING())

    for mcc in mccs:
        part_mcc += 1
        counts = 0
        # Try Authorizate MCC API
        auth = YeezyAPI().generate_auth(mcc['mcc_id'], mcc['mcc_token'])

        if not auth:
            await callback.message.edit_text(i18n.MCC.AUTH.FAIL(
                mcc_name=mcc['mcc_name']),
                reply_markup=kb_specific_back
            )
            return

        accounts_verify = [acc for acc in YeezyAPI().get_verify_accounts(auth['token']).get('accounts', []) if
                           acc['status'] in ('ACTIVE', 'RESTORED')]
        # accounts_unverify = [acc for acc in YeezyAPI().get_unverify_accounts(auth['token']).get('accounts', []) if
        #                      acc['status'] in ('ACTIVE', 'RESTORED')]

        accounts = accounts_verify  # + accounts_unverify

        for account in accounts:
            if not SubAccountRepository().account_by_uid(account['uid']):
                if not SubAccountRepository().add(
                        account_uid=account['uid'],
                        mcc_uuid=mcc['mcc_uuid'],
                        account_name="None",
                        account_email=account['email'],
                        account_timezone="None",
                        team_uuid="default",
                        team_name="default"
                ):
                    await callback.message.answer(i18n.ADMIN.SPECIFIC.LOAD.FAIL(
                        email=account['email'], mcc_name=mcc['mcc_name']
                    ))
                    continue
                counts += 1

        all_accounts += counts
        result += f"{mcc['mcc_name']}: <b>{counts}</b>\n"
        await callback.message.answer(f"{mcc['mcc_name']}: <b>{counts}</b> ({len(mccs)}\\{part_mcc})")

    await callback.message.answer(i18n.ADMIN.SPECIFIC.LOAD.RESULT(new_accounts=str(all_accounts), statistic=result))
