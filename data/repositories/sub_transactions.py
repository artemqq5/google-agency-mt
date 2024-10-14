from data.DefaultDataBase import DefaultDataBase


class SubTransactionRepository(DefaultDataBase):

    def transactions_by_team(self, team_uuid):
        query = "SELECT * FROM `sub_transactions` WHERE `team_uuid` = %s;"
        return self._select(query, (team_uuid,))

    def transaction(self, transaction_uuid):
        query = "SELECT * FROM `sub_transactions` WHERE `transaction_uuid` = %s;"
        return self._select_one(query, (transaction_uuid,))

    def add(self, value, transaction_uuid, balance_uuid, mcc_uuid, team_uuid, team_name):
        query = "INSERT INTO `sub_transactions` (`value`, `transaction_uuid`, `balance_uuid`, `mcc_uuid`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s, %s, %s);"
        return self._insert(query, (value, transaction_uuid, balance_uuid, mcc_uuid, team_uuid, team_name))

