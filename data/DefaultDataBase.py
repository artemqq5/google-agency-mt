import pymysql

from data.DefaultDataBaseTransaction import DefaultDataBaseTransaction
from private_config import DATABASE_PASSWORD, DATABASE_NAME


class DefaultDataBase(DefaultDataBaseTransaction):

    def __init__(self, con_transaction=None):
        super().__init__(con_transaction=con_transaction)
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password=DATABASE_PASSWORD,
            db=DATABASE_NAME,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def _insert(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_insert: {e}")

    def _update(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_update: {e}")

    def _delete(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_delete: {e}")

    def _select_one(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchone()
        except Exception as e:
            print(f"_select_one: {e}")

    def _select(self, query, args=None):
        try:
            with self.__connection as con:
                with con.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchall()
        except Exception as e:
            print(f"_select_all: {e}")

