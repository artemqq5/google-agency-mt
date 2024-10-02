from data.DefaultDataBase import DefaultDataBase


class AccessRepository(DefaultDataBase):

    def generate_accesss(self, access_uuid, team_uuid, team_name):
        query = "INSERT INTO `access` (access_uuid, team_uuid, team_name) VALUES (%s, %s, %s);"
        return self._insert(query, (access_uuid, team_uuid, team_name))

    # def get_access_by_uuid(self, access_uuid):
    #     query = "SELECT * FROM `access` WHERE `access_uuid` = %s;"
    #     return self._select_one(query, (access_uuid,))
    #
    def access_by_uuid(self, access_uuid):
        query = "SELECT * FROM `access` WHERE `access_uuid` = %s;"
        return self._select_one(query, (access_uuid,))

    def team_users_by_uuid(self, team_uuid):
        query = "SELECT * FROM `access` WHERE `team_uuid` = %s AND `user_id` IS NOT NULL;"
        return self._select(query, (team_uuid,))

    def activate_access(self, access_uuid, user_id, date_activated):
        query = "UPDATE `access` SET `activated` = %s, `user_id` = %s WHERE `access_uuid` = %s;"
        return self._update(query, (date_activated, user_id, access_uuid))

    def accesses_by_team_uuid(self, team_id):
        query = "SELECT * FROM `access` WHERE `team_uuid` = %s;"
        return self._select(query, (team_id,))
    #
    # def delete_access_by_uuid(self, access_uuid):
    #     query = "DELETE FROM `access` WHERE `access_uuid` = %s;"
    #     return self._delete(query, (access_uuid, ))

    # def delete_all_access_by_team_id(self, team_id):
    #     query = "DELETE FROM `access` WHERE `team_id` = %s;"
    #     return self._delete(query, (team_id,))

    # def update_access_status(self, access_uuid, access_status):
    #     query = "UPDATE `access` SET `status` = %s WHERE `access_uuid_` = %s;"
    #     return self._update(query, (access_status, access_uuid))


