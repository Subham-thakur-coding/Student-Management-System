import sqlite3
from db_config import Database
from validation import Validation
from update_all_details import Update_all_Details
from update_personal import Update_Personal_Details
class Update_student:
    def __init__(self):
        self.db = Database()
        self.valid = Validation()
        self.all = Update_all_Details()
        self.personal= Update_Personal_Details()
    # Update Menu logic
    def update_details(self):
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM student_details
                    """)
        
        fetch = cursor.fetchone()
        
        if not fetch:
            print("No Student Found!")
            
        while True:
            print("="*40)
            print(" WELCOME STUDENT DETAILS UPDATE MENU")
            print("="*40)
            print("1. Update all details")
            print("2. Update student's Personal Details")
            print("3. Back to Main Menu")
            
            choice: int = int(input("Enter your choice [1-3]: "))
            
            if choice == 1:
                self.all.update_all()
            elif choice == 2:
                self.personal.update_personal()
            elif choice == 3:
                break
            else:
                print("Invalid Input, TRY AGAIN!")