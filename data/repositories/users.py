from data.DefaultDataBase import DefaultDataBase
from data.constants import ADMIN, CLIENT


class UserRepository(DefaultDataBase):

    def add(self, user_id, username, firstname, lastname, lang):
        query = "INSERT INTO `users` (`user_id`, `username`, `firstname`, `lastname`, `lang`) VALUES (%s, %s, %s, %s, %s);"
        return self._insert(query, (user_id, username, firstname, lastname, lang))

    def user(self, user_id):
        query = "SELECT * FROM `users` WHERE `user_id` = %s;"
        return self._select_one(query, (user_id,))

    def users(self):
        query = "SELECT * FROM `users`;"
        return self._select(query)

    def admins(self):
        query = "SELECT * FROM `users` WHERE `role` = %s;"
        return self._select(query, ADMIN)

    def clients(self):
        query = "SELECT * FROM `users` WHERE `role` = %s;"
        return self._select(query, CLIENT)

    # temporary for update data in new structure tables database

    def update_lang(self, user_id, lang):
        query = "UPDATE `users` SET `lang` = %s WHERE `user_id` = %s;"
        return self._select_one(query, (lang, user_id))
