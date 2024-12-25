from asyncio.log import logger

from data.DefaultDataBase import DefaultDataBase
from data.repositories.balances import BalanceRepository
from data.repositories.mcc import MCCRepository
from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.taxes import TaxRepository


class TaxTransactionRepository(DefaultDataBase):
    def __init__(self):
        super().__init__()
        self.tax_repo = TaxRepository(self._connection_tran)
        self.balance_repo = BalanceRepository(self._connection_tran)
        self.sub_accounts_repo = SubAccountRepository(self._connection_tran)

    def add_tax_transaction(self, tax):
        """
        Синхронізує транзакцію з командою та зписує баланс з mcc команди, потім додає транзакцію в базу
        """
        try:
            # Починаємо транзакцію
            self._connection_tran.begin()

            sub_account = self.sub_accounts_repo.account_by_email_trans(tax['Google email'])
            if not sub_account:
                raise Exception(f"Error: unable to find account by email {tax['Google email']}")

            if not self.balance_repo.minus_trans(tax['Amount'], sub_account['mcc_uuid'], sub_account['team_uuid']):
                raise Exception("Error: unable to subtract balance")

            if not self.tax_repo.add_trans(
                    sub_account['team_name'], sub_account['team_uuid'], sub_account['mcc_uuid'],
                    tax['ID'], tax['Kind'], tax['Amount'], tax['Currency'], tax['Status'], tax['Google email'],
                    tax['Client link'], tax['description'], tax['Date']):
                raise Exception(f"Error: unable to add tax to db {tax}")

            # Коміт транзакції, якщо все успішно
            self._commit()

            return {"result": True, "taxID": tax['ID']}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logger.error(f"Transaction failed: {e}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()

