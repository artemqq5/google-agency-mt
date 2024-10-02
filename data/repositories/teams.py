from data.DefaultDataBase import DefaultDataBase


class TeamRepository(DefaultDataBase):

    def create_team(self, team_name, team_uuid, mcc_limit):
        query = "INSERT INTO `teams` (team_name, team_uuid, mcc_limit) VALUES (%s, %s, %s);"
        return self._insert(query, (team_name, team_uuid, mcc_limit))

    def team_by_id(self, team_id):
        query = "SELECT * FROM `teams` WHERE `team_id` = %s;"
        return self._select_one(query, (team_id,))

    def team_by_uuid(self, team_uuid):
        query = "SELECT * FROM `teams` WHERE `team_uuid` = %s;"
        return self._select_one(query, (team_uuid,))

    def teams(self):
        query = "SELECT * FROM `teams` ORDER BY `team_id` DESC;"
        return self._select(query)

    def delete_team(self, team_id):
        query = "DELETE FROM `teams` WHERE `team_id` = %s;"
        return self._delete(query, (team_id,))

    def update_team_mcc_limit(self, team_id, limit):
        query = "UPDATE `teams` SET `mcc_limit` = %s WHERE `team_id` = %s;"
        return self._update(query, (limit, team_id))
