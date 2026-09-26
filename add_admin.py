from validation import Validation
from autid_log import add_audit_log
from db_config import Database
import sqlite3
class Add_Admin:
    def __init__(self) -> None:
        self.valid = Validation()
        self.db = Database()
    

    # Add admin
    def add_admin(self):
        
        print("\n========== ADD ADMIN ==========")

        while True:
            user_id: str = input("Enter user ID: ")
            if self.valid.validate_user_id(user_id):
                break
            else:
                print("Invalid User ID!")
                print("User ID must contain at least 4 alphabets and 2 digits.")
        while True:
            password: str = input("Enter Password: ")
            if self.valid.validate_password(password):
                break
            else:
                print("Invalid Password!")
                print("Password must contain at least 4 alphabets, 2 digits and 2 allowed special characters.")
        
        con : sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("SELECT user_id FROM user_auth WHERE user_id = ?", (user_id,))
        
        ex_user = cursor.fetchone()
        if ex_user:
            print(f"{user_id} already exsist in dataase try with different id.")
            con.close()
            return False
        
        cursor.execute("""
                    INSERT INTO user_auth (user_id, password, user_role) VALUES (?, ?, ?)
                    """, (user_id, password, "employee"))
        con.commit()
        add_audit_log("NEW ADMIN ADDED",f"User ID: {user_id}, adeed into database")
        try:
            con.close()
            print(f"\n{'Admin details successfully added into database.':<20} || {'Now you can logged into portal with new user id and password!':<20}")
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            # back-up if database error raise then it will run
            # with open("admin_backup.csv", "a", newline="") as file:
            #     writer = csv.writer(file)
            #     if file.tell() == 0:
            #         writer.writerow(["user_id", "password"])
            #     writer.writerow([user_id, password])
            #     print("Admin details request saved in CSV file")
            #     print("\nAfter sometime it will be automatically  added in database when data base is active!. THANK YOU!")
            #     print("-"*40)
            return True