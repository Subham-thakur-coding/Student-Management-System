import sqlite3
from db_config import Database
class Add_Admin:
    def __init__(self) -> None:
        self.db = Database()
    def add_admin(self):
        while True:
            user_id: str = input("Enter youe user id: ")
            con: sqlite3.Connection = self.db.create_connection()
            cursor: sqlite3.Cursor = con.cursor()
            cursor.execute("""
                        SELECT
                        user_id,
                        user_role
                        FROM user_auth
                        WHERE user_id =?
                        """, (user_id,))
            fetch = cursor.fetchone()
            if not fetch:
                print(f"No user found for id {user_id}")
                return False

            print("\n*** USER FOUND ***")
            print(f"User Id: {fetch[0]}")
            print(f"User Current Role: {fetch[1]}\n")
            user_role: str = input("Enter user role [Employee/Payment]: ")
            cursor.execute("""
                        UPDATE
                        user_auth
                        SET user_role =?
                        WHERE user_id =?
                        """, (user_role, user_id))
            con.commit()
            print(f"\n Update successfully done for user id {user_id} and updated role {user_role}")

obj= Add_Admin()
obj.add_admin()