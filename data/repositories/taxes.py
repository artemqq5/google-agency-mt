from data.DefaultDataBase import DefaultDataBase


class TaxRepository(DefaultDataBase):

    def add_trans(self, team_name, team_uuid, mcc_uuid, transaction_uuid, kind, amount, currency, status, email,
                  client_link, desc, date):
        query = ("INSERT INTO `taxes` (team_name, team_uuid, mcc_uuid, transaction_uuid, kind, amount, currency,"
                 " status, email, client_link, `desc`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        return self._insert_tran(query, (team_name, team_uuid, mcc_uuid, transaction_uuid, kind, amount,
                                         currency, status, email, client_link, desc, date))

    def get(self, transaction_uuid):
        query = "SELECT * FROM `taxes` WHERE `transaction_uuid` = %s LIMIT 1;"
        return self._select_one(query, (transaction_uuid,))
