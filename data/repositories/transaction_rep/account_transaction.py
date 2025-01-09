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
            # Починаємо транзакцію
            self._connection_tran.begin()

            # Зменшуємо баланс
            if not self.balance_repo.minus_trans(data['amount'], data['mcc_uuid'], data['team_uuid']):
                raise Exception("Error: unable to subtract balance")

            # Зменшуємо кількість доступних акаунтів
            if not self.mcc_access_repo.minus_one_by_uuid(data['mcc_uuid'], data['team_uuid']):
                raise Exception("Error: unable to decrement available accounts")

            # Виконуємо API-запит для створення акаунту
            create_account_api = create_account_api_func()
            if not create_account_api or bool(create_account_api.get('state', False)) is False:
                error = create_account_api.get('errors', " ")
                raise Exception(f"Error: API request to create account failed | Optional:\n{error}")

            # Коміт транзакції, якщо все успішно
            self._commit()

            # Додаємо акаунт у базу даних
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
                raise Exception("Error: unable to add account to database")

            return {"result": True, "account_uid": create_account_api['account']['uid']}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()

    @staticmethod
    def create_account_transaction_admin(data, create_account_api_func, timezone):
        """
        Виконує транзакцію створення акаунту, знімає баланс, зменшує доступні акаунти та додає новий акаунт.
        """
        try:
            # Виконуємо API-запит для створення акаунту
            create_account_api = create_account_api_func()
            if not create_account_api or bool(create_account_api.get('state', False)) is False:
                error = create_account_api.get('errors', " ")
                raise Exception(f"Error: API request to create account failed | Optional:\n{error}")

            # Додаємо акаунт у базу даних
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
                raise Exception("Error: unable to add account to database")

            return {"result": True, "account_uid": create_account_api['account']['uid']}

        except Exception as e:
            # Відкат транзакції у разі помилки
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

    def refund_transaction_client(self, auth, data):
        """
        Виконує транзакцію рефаунду акаунта
        """
        try:
            # Починаємо транзакцію
            self._connection_tran.begin()

            # request to get actual account balance
            account = YeezyAPI().get_verify_account(auth['token'], data['account_uid'])['accounts'][0]

            print(account['balance'])
            print(account['balance'] * 0.96)

            refund_balance = round(account['balance'] * 0.96, 3)

            if not self.balance_repo.add_trans(refund_balance, data['mcc_uuid'], data['team_uuid']):
                raise Exception("Error: can`t refund balance to database")

            if not self.sub_accounts_repo.delete_account_trans(data['account_uid']):
                raise Exception("Error: can`t refund account from database")

            accdata = data['account']
            if not self.sub_accounts_repo.add_ref_account_trans(
                    accdata['account_uid'], accdata['mcc_uuid'], accdata['account_name'], accdata['account_email'],
                    accdata['account_timezone'], accdata['team_uuid'], accdata['team_name']):
                raise Exception("Error: can`t add account to refunded accounts database")

            if not YeezyAPI().refund(auth['token'], data['account_uid']):
                raise Exception("Error: can`t refund balance to MCC with API")

            # Коміт транзакції, якщо все успішно
            self._commit()

            return {"result": True, "account": account}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()

    def topup_account_transaction_client(self, auth, data):
        """
        Виконує транзакцію поповнення акаунту з головного MCC
        """
        try:
            # Починаємо транзакцію
            self._connection_tran.begin()

            if not self.balance_repo.minus_trans(data['value'], data['mcc_uuid'], data['team_uuid']):
                raise Exception("Error: can`t minus balance to topup account")

            # generate UUID for transaction
            transation_uuid = uuid.uuid4()

            if not self.sub_transactions_repo.add_sub_transaction(
                    data['value'], transation_uuid, data['balance_uuid'], data['mcc_uuid'], data['account_uid'],
                    data['team_uuid'], data['team_name']):
                raise Exception("Error: can`t add sub transaction about topup account to database")

            if not YeezyAPI().topup(auth['token'], data['account_uid'], data['value']):
                raise Exception("Error: can`t topup account from MCC with API")

            # Коміт транзакції, якщо все успішно
            self._commit()

            return {"result": True}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()
