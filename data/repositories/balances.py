from data.DefaultDataBase import DefaultDataBase


class BalanceRepository(DefaultDataBase):

    def balance(self, mcc_uuid, team_uuid):
        query = "SELECT * FROM `balances` WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._select_one(query, (mcc_uuid, team_uuid))

    def create(self, balance_uuid, mcc_uuid, team_uuid, team_name):
        query = "INSERT INTO `balances` (`balance_uuid`, `mcc_uuid`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (balance_uuid, mcc_uuid, team_uuid, team_name))
