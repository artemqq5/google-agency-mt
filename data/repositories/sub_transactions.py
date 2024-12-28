from data.DefaultDataBase import DefaultDataBase


class SubTransactionRepository(DefaultDataBase):

    def transactions_by_team(self, team_uuid):
        query = "SELECT * FROM `sub_transactions` WHERE `team_uuid` = %s ORDER BY `id`;"
        return self._select(query, (team_uuid,))

    def transaction(self, transaction_uuid):
        query = "SELECT * FROM `sub_transactions` WHERE `transaction_uuid` = %s;"
        return self._select_one(query, (transaction_uuid,))

    # operation by transaction
    def add_sub_transaction(self, value, transaction_uuid, balance_uuid, mcc_uuid, sub_account_uid,  team_uuid, team_name):
        query = "INSERT INTO `sub_transactions` (`value`, `transaction_uuid`, `balance_uuid`, `mcc_uuid`, `sub_account_uid`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        return self._insert_tran(query, (value, transaction_uuid, balance_uuid, mcc_uuid, sub_account_uid, team_uuid, team_name))

