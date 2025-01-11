import uuid

from aiogram.utils.chat_action import logger

from data.DefaultDataBase import DefaultDataBase
from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.sub_transactions import SubTransactionRepository
from data.repositories.teams import TeamRepository


class AccountTransactionRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()
        self.mcc_access_repo = MCCAccessRepository(self._connection_tran)
        self.balance_repo = BalanceRepository(self._connection_tran)
        self.sub_accounts_repo = SubAccountRepository(self._connection_tran)
        self.sub_transactions_repo = SubTransactionRepository(self._connection_tran)

    def create_account_transaction(self, data, create_account_api_func, timezone):
        """
        Виконує транзакцію створення акаунту, знімає баланс, зменшує доступні акаунти та додає новий акаунт.
        """
        try:
            logger.info("Starting account creation transaction")
            self._connection_tran.begin()

            # Зменшуємо баланс
            logger.info(f"Reducing balance: {data['amount']} for MCC: {data['mcc_uuid']}, Team: {data['team_uuid']}")
            if not self.balance_repo.minus_trans(data['amount'], data['mcc_uuid'], data['team_uuid']):
                raise Exception("Unable to subtract balance")

            # Зменшуємо кількість доступних акаунтів
            logger.info(f"Decrementing available accounts for MCC: {data['mcc_uuid']}, Team: {data['team_uuid']}")
            if not self.mcc_access_repo.minus_one_by_uuid(data['mcc_uuid'], data['team_uuid']):
                raise Exception("Unable to decrement available accounts")

            # Виконуємо API-запит для створення акаунту
            logger.info("Calling API to create account")
            create_account_api = create_account_api_func()
            if not create_account_api or not create_account_api.get('state', False):
                error = create_account_api.get('errors', "No error details provided")
                raise Exception(f"API request to create account failed | Details: {error}")

            # Коміт транзакції
            logger.info("Committing transaction")
            self._commit()

            # Додаємо акаунт у базу даних
            logger.info("Adding account to the database")
            team = TeamRepository().team_by_uuid(data['team_uuid'])
            if not SubAccountRepository().add(
                    create_account_api['account']['uid'],
                    data['mcc_uuid'],
                    data['name'],
                    data['email'],
                    timezone,
                    data['team_uuid'],
                    team['team_name']
            ):
                raise Exception("Unable to add account to database")

            logger.info(f"Account created successfully with UID: {create_account_api['account']['uid']}")
            return {"result": True, "account_uid": create_account_api['account']['uid']}

        except Exception as e:
            self._rollback()
            logger.error(f"Transaction failed during account creation: {e}. Data: {data}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()
            logger.info("Transaction connection closed")

    @staticmethod
    def create_account_transaction_admin(data, create_account_api_func, timezone):
        try:
            logger.info("Starting admin account creation transaction")
            create_account_api = create_account_api_func()
            if not create_account_api or not create_account_api.get('state', False):
                error = create_account_api.get('errors', "No error details provided")
                raise Exception(f"API request to create account failed | Details: {error}")

            logger.info("Adding admin account to the database")
            team = TeamRepository().team_by_uuid(data.get('team_uuid', "no team")) or {}
            if not SubAccountRepository().add(
                    create_account_api['account']['uid'],
                    data['mcc_uuid'],
                    data['name'],
                    data['email'],
                    timezone,
                    data.get('team_uuid', 'default'),
                    team.get('team_name', 'default')
            ):
                raise Exception("Unable to add admin account to database")

            logger.info(f"Admin account created successfully with UID: {create_account_api['account']['uid']}")
            return {"result": True, "account_uid": create_account_api['account']['uid']}

        except Exception as e:
            logger.error(f"Admin account creation failed: {e}. Data: {data}")
            return {"result": False, "error": str(e)}

    def refund_transaction_client(self, auth, data):
        try:
            logger.info("Starting refund transaction")
            self._connection_tran.begin()

            logger.info("Fetching account details for refund")
            account = YeezyAPI().get_verify_account(auth['token'], data['account_uid'])['accounts'][0]
            refund_balance = round(account['balance'] * 0.96, 3)

            logger.info(f"Adding refunded balance: {refund_balance} to MCC: {data['mcc_uuid']}")
            if not self.balance_repo.add_trans(refund_balance, data['mcc_uuid'], data['team_uuid']):
                raise Exception("Unable to refund balance to database")

            logger.info(f"Deleting account with UID: {data['account_uid']} from the database")
            if not self.sub_accounts_repo.delete_account_trans(data['account_uid']):
                raise Exception("Unable to delete account from database")

            logger.info("Adding refunded account to refunded accounts database")
            accdata = data['account']
            if not self.sub_accounts_repo.add_ref_account_trans(
                    accdata['account_uid'], accdata['mcc_uuid'], accdata['account_name'], accdata['account_email'],
                    accdata['account_timezone'], accdata['team_uuid'], accdata['team_name']):
                raise Exception("Unable to add account to refunded accounts database")

            logger.info(f"Calling API to refund balance for account UID: {data['account_uid']}")
            if not YeezyAPI().refund(auth['token'], data['account_uid']):
                raise Exception("Unable to refund balance to MCC with API")

            self._commit()
            logger.info("Refund transaction completed successfully")
            return {"result": True, "account": account}

        except Exception as e:
            self._rollback()
            logger.error(f"Refund transaction failed: {e}. Data: {data}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()
            logger.info("Transaction connection closed")
