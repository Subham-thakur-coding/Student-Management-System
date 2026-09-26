import sqlite3
from db_config import Database
from autid_log import add_audit_log
class Search_Couse:
    def __init__(self) -> None:
        self.db = Database()
        
    # logic for search course details by Id
    def search_course(self):
        course_id: int = int(input("Enter course ID: "))
        
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM student_course
                    WHERE course_id =?
                    """,(course_id,))
        
        course = cursor.fetchone()
        con.commit()
        add_audit_log("COURSE SEARCH", f"{course_id}, course id details fetch database")
        if course == None:
            print(f"No course details found or no course added for course id: {course_id}")
            return False
        
        print("-"*20)
        print("\n*********** DETAILS FOUND ***********")
        print("-"*20)
        print(f"Course ID: {course[0]}\n")
        print(f"Course Name: {course[1]}\n")
        print(f"Course Duration: {course[2]}\n")
        print(f"Course Topics: {course[3]}\n")
