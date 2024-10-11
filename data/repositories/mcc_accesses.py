from data.DefaultDataBase import DefaultDataBase


class MCCAccessRepository(DefaultDataBase):

    def share_mcc(self, mcc_acccess_uuid, mcc_uuid, team_uuid, team_name):
        query = "INSERT INTO `mcc_accesses` (`mcc_access_uuid`, `mcc_uuid`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (mcc_acccess_uuid, mcc_uuid, team_uuid, team_name))

    def delete_mcc_access(self, mcc_uuid, team_uuid):
        query = "DELETE FROM `mcc_accesses` WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._delete(query, (mcc_uuid, team_uuid))

    def mcc_access(self, mcc_uuid, team_uuid):
        query = "SELECT * FROM `mcc_accesses` WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._select_one(query, (mcc_uuid, team_uuid))

    def mcc_accesses_by_team_uuid(self, team_uuid):
        query = "SELECT * FROM `mcc_accesses` WHERE `team_uuid` = %s;"
        return self._select(query, (team_uuid, ))

    def change_limit_by_uuid(self, limit, mcc_uuid, team_uuid):
        query = "UPDATE `mcc_accesses` SET `account_available` = %s WHERE `mcc_uuid` = %s AND `team_uuid` = %s;"
        return self._update(query, (limit, mcc_uuid, team_uuid))
