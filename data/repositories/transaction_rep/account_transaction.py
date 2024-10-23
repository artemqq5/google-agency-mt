from aiogram.utils.chat_action import logger

from data.DefaultDataBase import DefaultDataBase
from data.YeezyAPI import YeezyAPI
from data.repositories.balances import BalanceRepository
from data.repositories.mcc_accesses import MCCAccessRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.teams import TeamRepository
from domain.notification.admin_notify import NotificationAdmin


class AccountTransactionRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()
        self.mcc_access_repo = MCCAccessRepository(self._connection_tran)
        self.balance_repo = BalanceRepository(self._connection_tran)
        self.sub_accounts_repo = SubAccountRepository(self._connection_tran)

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
                raise Exception(f"Error: API request to create account failed\n\nOptional:\n{error}")

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
                return {"result": False, "error": "Error: unable to add account to database"}

            return {"result": True, "account_uid": create_account_api['account']['uid']}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()

    def create_account_transaction_admin(self, data, create_account_api_func, timezone):
        """
        Виконує транзакцію створення акаунту, знімає баланс, зменшує доступні акаунти та додає новий акаунт.
        """
        try:
            # Починаємо транзакцію
            self._connection_tran.begin()

            # Виконуємо API-запит для створення акаунту
            create_account_api = create_account_api_func()
            if not create_account_api or bool(create_account_api.get('state', False)) is False:
                error = create_account_api.get('errors', " ")
                raise Exception(f"Error: API request to create account failed\n\nOptional:\n{error}")

            # Коміт транзакції, якщо все успішно
            self._commit()

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
                return {"result": False, "error": "Error: unable to add account to database"}

            return {"result": True, "account_uid": create_account_api['account']['uid']}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()

    def refund_transaction_client(self, auth, data):
        try:
            # Починаємо транзакцію
            self._connection_tran.begin()

            # request to get actual account balance
            account = YeezyAPI().get_verify_account(auth['token'], data['account_uid'])['accounts'][0]

            if not self.balance_repo.add_trans(account['balance'], data['mcc_uuid'], data['team_uuid']):
                raise Exception("Error: can`t refund balance to database")

            if not self.sub_accounts_repo.delete_account_trans(data['account_uid']):
                raise Exception("Error: can`t delete account from database")

            if not YeezyAPI().refund(auth['token'], data['account_uid']):
                raise Exception("Error: can`t refund balance to MCC with API")

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

