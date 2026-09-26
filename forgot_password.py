import sqlite3
from db_config import Database
from validation import Validation
from autid_log import add_audit_log
class Forgot_Password:
    def __init__(self) -> None:
        self.db = Database()
        self.valid = Validation()
    # logic for forgot password
    def forgot(self):
        while True:
            user_id: str = input("Enter your user id: ")
            if self.valid.validate_user_id(user_id):
                break
            print(f"Invalid User Id or Defult password can be modify! {user_id}")

        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        try:
            cursor.execute("""
                        SELECT user_id
                        FROM user_auth
                        WHERE user_id = ?
                        """,(user_id,))
            fetch = cursor.fetchone()
            if not fetch:
                print(f"No user ID found {user_id}")
                return False
            print(f"\nYou'r changing password for the user id  {user_id}")
            
            while True:
                new_password: str = input("\nEnter new password: ")
                confirm_password: str = input("\nConfirm new password: ")
                if not self.valid.validate_password(confirm_password):
                    print("❌ Invalid password format.")
                    continue
                if new_password != confirm_password:
                    print("❌ Passwords do not match. Please try again.")
                    continue
                print("\n✅ Passwords matched! ✅")
                break
            alert: str = input("Are you confirm to commit the changes [yes/no]: ").lower()
            if alert == "no":
                print("\n❌Operation aborted❌")
                return False
            cursor.execute("""
                        UPDATE user_auth
                        SET password =?
                        WHERE user_id =?
                        """,(new_password, user_id))
            con.commit()
            add_audit_log("PASSWORD CHANGE BY ADMIN",f"User ID: {user_id}, password changed")
            print("\n✅Password changed successfully!✅")
            print("*** Please login with your new password. ***")

        except sqlite3.Error as e:
            con.close()
            print(f"Database Error {e}")
            

# obj= Forgot_Password()
# obj.forgot()