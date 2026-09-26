import sqlite3
from db_config import Database
from autid_log import add_audit_log
class Display_Payment:
    def __init__(self) -> None:
        self.db = Database()
        
    # logic for display payment
    def display_payment(self):
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM payment_details
                    """)
        fetch: list = cursor.fetchall()
        con.commit()
        add_audit_log("PAYMENT DETAILS FETCH","Payment details fetch from database.")
        if len(fetch) == 0:
            print("No payment details added!")
            con.close()
            return False
        print("-"*110)
        print("\nAdmission Details Found")
        print("-"*110)
        print(
            f"{'\nStudent ID':<12}"
            f"{'Payment ID':<12}"
            f"{'Amount':<15}"
            f"{'Admission Status':<20}"
            f"{'Payment Method':<20}"
            f"{'Last Updated'}"
        )
        print("-"*110)
        for details in fetch:
            print(
            f"{details[0] :<12}"
            f"{details[1] :<12}"
            f"{details[2] :<15}"
            f"{details[3] :<20}"
            f"{details[4] :<20}"
            f"{details[5]}"
            )
            
        try:
            con.close()
        except sqlite3.Error as e:
            print(f"Database Error {e}")
            
# obj = Display_Payment()
# obj.display_payment()
