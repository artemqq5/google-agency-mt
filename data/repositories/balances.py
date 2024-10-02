from data.DefaultDataBase import DefaultDataBase


class BalanceRepository(DefaultDataBase):

    def create(self, balance_uuid, mcc_uuid, team_uuid):
        query = "INSERT INTO `balances` (`balance_uuid`, `mcc_uuid`, `team_uuid`) VALUES (%s, %s, %s);"
        return self._insert(query, (balance_uuid, mcc_uuid, team_uuid))

