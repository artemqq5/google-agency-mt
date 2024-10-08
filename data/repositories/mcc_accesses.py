from data.DefaultDataBase import DefaultDataBase


class MCCAccessRepository(DefaultDataBase):

    def share_mcc(self, mcc_acccess_uuid, mcc_uuid, team_uuid, team_name):
        query = "INSERT INTO `mcc_accesses` (`mcc_access_uuid`, `mcc_uuid`, `team_uuid`, `team_name`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (mcc_acccess_uuid, mcc_uuid, team_uuid, team_name))
