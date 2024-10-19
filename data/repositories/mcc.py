from data.DefaultDataBase import DefaultDataBase


class MCCRepository(DefaultDataBase):

    def generals_mcc(self):
        query = "SELECT * FROM `mcc` WHERE `is_general` = 1;"
        return self._select(query)

    def update_general(self, mcc_uuid, general):
        query = "UPDATE `mcc` SET `is_general` = %s WHERE `mcc_uuid` = %s;"
        return self._update(query, (general, mcc_uuid))

    def add(self, mcc_uuid, mcc_name, mcc_id, mcc_token):
        query = "INSERT INTO `mcc` (`mcc_uuid`, `mcc_name`, `mcc_id`, `mcc_token`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (mcc_uuid, mcc_name, mcc_id, mcc_token))

    def mccs(self):
        query = "SELECT * FROM `mcc`;"
        return self._select(query)

    def available_mccs_by_team_uuid(self, team_uuid):
        query = "SELECT mcc.* FROM `mcc` LEFT JOIN `mcc_accesses` ON `mcc`.`mcc_uuid` = `mcc_accesses`.`mcc_uuid` AND `mcc_accesses`.`team_uuid` = %s WHERE `mcc_accesses`.`mcc_uuid` IS NULL;"
        return self._select(query, (team_uuid, ))

    def mcc_by_uuid(self, mcc_uuid):
        query = "SELECT * FROM `mcc` WHERE `mcc_uuid` = %s;"
        return self._select_one(query, (mcc_uuid,))

    def mccs_by_team_uuid(self, team_uuid):
        query = "SELECT mcc.* FROM `mcc` JOIN `mcc_accesses` ON `mcc`.`mcc_uuid` = `mcc_accesses`.`mcc_uuid` WHERE `mcc_accesses`.`team_uuid` = %s;"
        return self._select(query, (team_uuid, ))
