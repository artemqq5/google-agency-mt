from data.DefaultDataBase import DefaultDataBase


class MCCRepository(DefaultDataBase):

    def generals_mcc(self):
        query = "SELECT * FROM `mcc` WHERE `is_general` = 1;"
        return self._select(query)
