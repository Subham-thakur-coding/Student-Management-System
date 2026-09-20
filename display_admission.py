import sqlite3
from db_config import Database

class Display_admission:
    def __init__(self) -> None:
        self.db = Database()
        
    # logic for display admission
    def display_admission(self):
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM student_admission
                    """)
        respose: list = cursor.fetchall()
        
        if len(respose) == 0:
            con.close()
            print("No Admission details found!")
            return False
        print("-"*80)
        print("\nAdmission Details Found")
        print("-"*80)
        print(
            f"{'\nAdmission ID':<20}"
            f"{'Student ID':<20}"
            f"{'Admission Status'}"
        )
        print("-"*80)
        for details in respose:
            print(
            f"{details[0]:<20}"
            f"{details[1]:<20}"
            f"{details[2]}"
            )
