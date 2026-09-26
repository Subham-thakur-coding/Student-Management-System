import sqlite3
from db_config import Database
from user_session import UserSession
from autid_log import add_audit_log
from main_menu import Main_Menu
class Menu:
    def __init__(self):
        self.db= Database()
        self.menu = Main_Menu()

    # Login cridential
    def login(self):
        print("\n")
        print("=" * 60)
        print(f"\n{'STUDENT MANAGEMENT ADMIN PORTAL':<20} || {'Version No. 3.0.0 beta':<20}\n")
        print("\n***Connection Status with Database: ACTIVE!***")
        print("=" * 60)
        while True:

            user_id = input("Enter User ID: ")
            print("-" * 50)
            password = input("Enter Password: ")
            print("-" * 50)
            self.db.create_table()
            # Authenticate user
            con: sqlite3.Connection = self.db.create_connection()
            cursor: sqlite3.Cursor = con.cursor()
            
            cursor.execute("""
                        SELECT user_id, user_role
                        FROM user_auth
                        WHERE user_id =? AND password =?
                        """,(user_id, password))
            
            fetch = cursor.fetchone()
            # if login successfully
            if fetch:
                # fetch[0] = user_id (fetch return a tuple so we have to access it by indexing)
                # fetch[1] = role
                UserSession.login(
                    fetch[0],
                    fetch[1]
                )
                # note audit log
                add_audit_log(
                    "LOGIN",
                    f"{fetch[0]} logged into the system"
                )
                print("\n*** Login Successfully! ***")
                print(f"User ID : {UserSession.get_user()}")
                print(f"Role    : {UserSession.get_role()}")
                self.menu.main_menu()
                return True

            else:
                print("\nInvalid User ID or Password!")
                print("-" * 50)
                print("1. Try Again")
                print("-" * 50)
                print("2. Exit")
                print("-" * 50)
                try:
                    choice = int(input("Enter your choice: "))
                except ValueError as e:
                    print(f"\n{e} a invalid number.")
                    continue
                if choice == 1:
                    continue
                elif choice == 2:
                    print("\nThank you!")
                    return False
                else:
                    print("\nInvalid choice!")

    # Program start from here 
    def start_program(self):
        self.login()

if __name__ == "__main__":
    obj = Menu()
    obj.start_program()