import sqlite3
from db_config import Database
from autid_log import add_audit_log
class Delete:
    def __init__(self):
        self.db = Database()
    # Delete Student
    def delete_student(self):
        student_id: int = int(input("Enter Student ID: "))
        
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM student_details
                    WHERE student_id =?
                    """,(student_id,))
        response = cursor.fetchone()
        
        if response is None:
            print("Student not Found!")
            con.close()
            return
        
        else:
            choice:str = input("Are you sure![yes/no]").lower()
            if choice == "no":
                print("\nOperation Forbidden!")
                con.close()
                return False
            # delete admission
            cursor.execute("""
                        DELETE FROM student_admission
                        WHERE student_id =?
                        """,(student_id,))
            
            # Delete student
            cursor.execute("""
                        DELETE FROM student_details
                        WHERE student_id =?
                        """,(student_id,))
            # delete payment
            cursor.execute("""
                        DELETE FROM payment_details
                        WHERE student_id =?
                        """,(student_id,))
            con.commit()
            add_audit_log("STUDENT DELETED",f"{student_id}, deleted from database")
            try:
                print("-"*20)
                print("Details delete successfully!")
                print("-"*20)
            except sqlite3.Error as error:
                con.close()
                print(f"Check your code error is {error}")
                
# object create
Obj_delete_student = Delete()