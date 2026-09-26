import sqlite3
from db_config import Database
from autid_log import add_audit_log
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
        con.commit()
        add_audit_log("ADMISSION DETAILS FETCH","Admission details fetch from database.")
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
        try:
            con.close()
        except sqlite3.Error as e:
            print(f"Database Error {e}")