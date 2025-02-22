from data.DefaultDataBase import DefaultDataBase


class BalanceRepository(DefaultDataBase):

    def __init__(self, con_transaction=None):
        super().__init__(con_transaction)

    def add(self, value, mcc_uuid, team_uuid):
        query = "UPDATE `balances` SET `balance` = `balance` + %s  WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._update(query, (value, mcc_uuid, team_uuid))

    def minus(self, value, mcc_uuid, team_uuid):
        query = "UPDATE `balances` SET `balance` = `balance` - %s  WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._update(query, (value, mcc_uuid, team_uuid))

    # safe method by transaction
    def minus_trans(self, value, mcc_uuid, team_uuid):
        query = "UPDATE `balances` SET `balance` = `balance` - %s  WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._update_tran(query, (value, mcc_uuid, team_uuid))

    def add_trans(self, value, mcc_uuid, team_uuid):
        query = "UPDATE `balances` SET `balance` = `balance` + %s  WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._update_tran(query, (value, mcc_uuid, team_uuid))

    def balance(self, mcc_uuid, team_uuid):
        query = "SELECT * FROM `balances` WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._select_one(query, (mcc_uuid, team_uuid))

    def create(self, balance_uuid, mcc_uuid, team_uuid, team_name):
        query = "INSERT INTO `balances` (`balance_uuid`, `mcc_uuid`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (balance_uuid, mcc_uuid, team_uuid, team_name))
