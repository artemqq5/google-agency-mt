from data.DefaultDataBase import DefaultDataBase


class MCCRepository(DefaultDataBase):

    def generals_mcc(self):
        query = "SELECT * FROM `mcc` WHERE `is_general` = 1;"
        return self._select(query)

    def add(self, mcc_uuid, mcc_name, mcc_id, mcc_token):
        query = "INSERT INTO `mcc` (`mcc_uuid`, `mcc_name`, `mcc_id`, `mcc_token`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (mcc_uuid, mcc_name, mcc_id, mcc_token))

    def mccs(self):
        query = "SELECT * FROM `mcc`;"
        return self._select(query)


