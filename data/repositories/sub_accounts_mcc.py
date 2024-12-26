from data.DefaultDataBase import DefaultDataBase


class SubAccountRepository(DefaultDataBase):

    def __init__(self, con_transaction=None):
        super().__init__(con_transaction)

    def account_by_uid(self, account_uid):
        query = "SELECT * FROM `sub_accounts` WHERE `account_uid` = %s;"
        return self._select_one(query, (account_uid,))

    def account_by_email(self, account_email):
        query = "SELECT * FROM `sub_accounts` WHERE `account_email` = %s;"
        return self._select_one(query, (account_email,))

    def accounts_by_mcc_uuid(self, mcc_uuid):
        query = "SELECT * FROM `sub_accounts` WHERE `mcc_uuid` = %s ORDER BY `created` DESC;"
        return self._select(query, (mcc_uuid,))

    def accounts_by_team_uuid(self, mcc_uuid, team_uuid):
        query = "SELECT * FROM `sub_accounts` WHERE `mcc_uuid` = %s AND `team_uuid` = %s ORDER BY `created` DESC;"
        return self._select(query, (mcc_uuid, team_uuid))

    def update_email_by_uid(self, email, uid):
        query = "UPDATE `sub_accounts` SET `account_email` = %s WHERE `account_uid` = %s;"
        return self._update(query, (email, uid))

    def add(self, account_uid, mcc_uuid, account_name, account_email, account_timezone, team_uuid, team_name):
        query = ("INSERT INTO `sub_accounts` (`account_uid`, `mcc_uuid`, `account_name`, `account_email`,"
                 " `account_timezone`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s, %s, %s, %s);")
        return self._insert(
            query,
            (account_uid, mcc_uuid, account_name, account_email, account_timezone, team_uuid, team_name)
        )

    def update_team(self, team_uuid, team_name, account_uid):
        query = "UPDATE `sub_accounts` SET `team_uuid` = %s, `team_name` = %s WHERE `account_uid` = %s;"
        return self._update(query, (team_uuid, team_name, account_uid))

    def delete_account_trans(self, account_uid):
        query = "DELETE FROM `sub_accounts` WHERE `account_uid` = %s;"
        return self._delete_tran(query, (account_uid,))
