from data.DefaultDataBase import DefaultDataBase


class TransactionRepository(DefaultDataBase):

    def transactions_by_team(self, team_uuid):
        query = "SELECT * FROM `transactions` WHERE `team_uuid` = %s;"
        return self._select(query, (team_uuid,))
