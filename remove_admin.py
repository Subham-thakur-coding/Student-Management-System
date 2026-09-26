import sqlite3
from db_config import Database
from autid_log import add_audit_log
class Remove_Admin:
    def __init__(self) -> None:
        self.db = Database()
    # Remove Admin
    def remove_admin(self):
        user_id :str = input("Enter User ID: ")
        password: str = input("Enter your Password:")

        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        cursor.execute("""
                    SELECT * FROM user_auth
                    WHERE user_id = ? AND password =?
                    """,(user_id, password))
        fetch = cursor.fetchone()
        if fetch is None:
            print("-"*50)
            print("Cridential Mismatch")
            print("-"*50)
            con.close()
            return False
        cursor.execute("""
                    DELETE FROM user_auth
                    WHERE user_id =? AND password=?
                    """,(user_id, password))
        con.commit()
        add_audit_log("ADMIN REMOVED",f"User ID: {user_id}, removed from database")
        try:
            con.close()
            print(f"\tUser ID: {user_id} removed from database!")
        except sqlite3.Error as e:
            print(f"Database Error: {e}")