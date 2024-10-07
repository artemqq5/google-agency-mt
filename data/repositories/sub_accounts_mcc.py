from data.DefaultDataBase import DefaultDataBase


class SubAccountMCC(DefaultDataBase):

    def accounts_by_mcc_uuid(self, mcc_uuid):
        query = "SELECT * FROM `sub_accunts` WHERE `mcc_uuid` = %s;"
        return self._select(query, (mcc_uuid,))
