from data.DefaultDataBase import DefaultDataBase


class SubAccountRepository(DefaultDataBase):

    def account_by_uid(self, account_uid):
        query = "SELECT * FROM `sub_accounts` WHERE `account_uid` = %s;"
        return self._select_one(query, (account_uid,))

    def accounts_by_mcc_uuid(self, mcc_uuid):
        query = "SELECT * FROM `sub_accounts` WHERE `mcc_uuid` = %s;"
        return self._select(query, (mcc_uuid,))

    def accounts_by_team_uuid(self, mcc_uuid, team_uuid):
        query = "SELECT * FROM `sub_accounts` WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._select(query, (mcc_uuid, team_uuid))

    def update_email_by_uid(self, email, uid):
        query = "UPDATE `sub_accounts` SET `account_email` = %s WHERE `account_uid` = %s;"
        return self._update(query, (email, uid))
