import sqlite3
from db_config import Database
from validation import Validation
class Modify_admission:
    def __init__(self) -> None:
        self.db = Database()
        self.valid= Validation()
    # logic for modify admission status
    def update_status(self):
        student_id: int = int(input("Enter your Student Id: "))
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM student_admission
                    WHERE student_id =?
                    """,(student_id,))
        
        respose = cursor.fetchone()
        
        if respose is None:
            con.close()
            print("No Admission Details found or details not added!")
            return False
        print("-"*50)
        print("Details Found!")
        print("-"*50)
        print(f"Admission Id: {respose[0]}")
        print(f"Student Id: {respose[1]}")
        print(f"Admission Status: {respose[2]}")
        while True:
            admission: str = input("Enter Updated Admission Status[Pending|Approved|Rejected]: ").capitalize()
            if self.valid.validate_status(admission):
                break
            print("Invalid Status!")
        cursor.execute("""
                    UPDATE student_admission
                    SET admission_status =?
                    WHERE student_id =?
                    """,(admission, student_id))
        try:
            con.commit()
            print("Data Update Successfully!")
        except sqlite3.Error as e:
            print(f"Database Error {e}")
        finally:
            con.close()
                
