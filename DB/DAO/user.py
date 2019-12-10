from DAO.index import *
from DTO.user import *
from SQL.user import UserSQL as SQL


class UserDAO(Index):
    def select_index(self, user):
        return self.execute_sql_for_one_result(user, SQL.SELECT_INDEX)

    def select_user_by_email(self, email):
        try:
            conn = self.db_conn.get_connection()
            cursor = conn.cursor()

            cursor.execute(SQL.SELECT_USER, email)
            result = cursor.fetchone()

            user = User()
            user.set_all(result)

            self.db_conn.close_db()
            return user

        except Exception as e:
            return e

    def is_existing_email(self, email):
        if self.execute_sql_for_one_result(email, SQL.CHECK_EMAIL) == 1:
            return True
        else:
            return False
