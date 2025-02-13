from data.DefaultDataBase import DefaultDataBase


class TaxRepository(DefaultDataBase):

    def add_trans(self, team_name, mcc_name, team_uuid, mcc_uuid, transaction_uuid, kind, amount, currency, status,
                  email, client_link, desc, date):
        query = ("INSERT INTO `taxes` ("
                 "team_name, mcc_name, team_uuid, mcc_uuid, transaction_uuid, kind, amount, currency, "
                 "status, email, client_link, `desc`, `date`"
                 ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        return self._insert_tran(query, (team_name, mcc_name, team_uuid, mcc_uuid, transaction_uuid, kind, amount,
                                         currency, status, email, client_link, desc, date))

    def get(self, transaction_uuid):
        query = "SELECT * FROM `taxes` WHERE `transaction_uuid` = %s LIMIT 1;"
        return self._select_one(query, (transaction_uuid,))

    def taxes_by_team(self, team_uuid):
        query = "SELECT * FROM `taxes` WHERE `team_uuid` = %s ORDER BY `id` DESC;"
        return self._select(query, (team_uuid,))

    def taxes(self):
        query = "SELECT * FROM `taxes`;"
        return self._select(query)