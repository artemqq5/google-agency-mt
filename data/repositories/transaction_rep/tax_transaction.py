import logging

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

    def add_tax_transaction(self, tax):
        """
        Синхронізує транзакцію з командою та зписує баланс з mcc команди, потім додає транзакцію в базу
        """
        try:
            logging.info(f"Starting tax transaction for tax ID: {tax['ID']} and Google email: {tax['Google email']}")

            # Починаємо транзакцію
            self._begin_transaction()
            logging.info("Transaction begun successfully")

            # Отримуємо обліковий запис за email
            logging.info(f"Searching for account by email: {tax['Google email']}")
            sub_account = SubAccountRepository().account_by_email(tax['Google email'])
            if not sub_account:
                logging.info(f"No active account found. Searching in refunded accounts for email: {tax['Google email']}")
                sub_account = SubAccountRepository().ref_account_by_email(tax['Google email'])
                if not sub_account:
                    logging.error(f"Account not found by email: {tax['Google email']}")
                    raise Exception(f"Error: unable to find account by email {tax['Google email']}")

            logging.info(f"Account found: {sub_account}")

            # Отримуємо MCC за UUID
            logging.info(f"Fetching MCC details for UUID: {sub_account['mcc_uuid']}")
            mcc_account = MCCRepository().mcc_by_uuid(sub_account['mcc_uuid'])
            if not mcc_account:
                logging.error(f"MCC not found by UUID: {sub_account['mcc_uuid']}")
                raise Exception(f"Error: unable to find MCC by UUID {sub_account['mcc_uuid']}")

            logging.info(f"MCC details: {mcc_account}")

            # Знімаємо баланс
            logging.info(f"Subtracting amount {tax['Amount']} from MCC UUID: {sub_account['mcc_uuid']} and Team UUID: {sub_account['team_uuid']}")
            if not self.balance_repo.minus_trans(tax['Amount'], sub_account['mcc_uuid'], sub_account['team_uuid']):
                logging.error(f"Error subtracting balance. Tax details: {tax}")
                raise Exception(f"Error: unable to subtract balance for email {tax['Google email']}")

            logging.info(f"Balance subtracted successfully for MCC UUID: {sub_account['mcc_uuid']}")

            # Додаємо транзакцію до бази даних
            logging.info("Adding tax transaction to database")
            if not self.tax_repo.add_trans(
                sub_account['team_name'], mcc_account['mcc_name'], sub_account['team_uuid'], sub_account['mcc_uuid'],
                tax['ID'], tax['Kind'], tax['Amount'], tax['Currency'], tax['Status'], tax['Google email'],
                tax['Client link'], tax['description'], tax['Date']
            ):
                logging.error(f"Failed to add tax to database for email {tax['Google email']}. Tax may already exist.")
                raise Exception(f"Error: unable to add tax to db {tax['Google email']} Maybe it already exists")

            logging.info(f"Tax transaction added successfully to database for tax ID: {tax['ID']}")

            # Коміт транзакції
            self._commit()
            logging.info("Transaction committed successfully")

            return {"result": True, "taxID": tax['ID'], "mcc_name": mcc_account['mcc_name']}

        except Exception as e:
            # Відкат транзакції у разі помилки
            self._rollback()
            logging.error(f"Transaction failed: {e}. Tax data: {tax}")
            return {"result": False, "error": str(e)}

        finally:
            self._close()
            logging.info("Transaction connection closed")
