import sqlite3
from db_config import Database

class Display_Course:
    def __init__(self):
        self.db = Database()
        
    # Logic for dispaly course details
    def display_course(self):
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM student_course
                    """)
        courses: list = cursor.fetchall()
        
        if len(courses) == 0:
            print("No Course Found, add student first then course will automatically added!")
            con.close()
            return False
        print("-"*80)
        print("\nCourse Details Found")
        print("-"*80)
        print(
            f"{'\nID':<10}"
            f"{'Course Name':<20}"
            f"{'Course Duration':<25}"
            f"{'Course Topic\n'}"
        )
        print("-"*80)
        
        for course in courses:
            print(
                f"{course[0]:<10}"
                f"{course[1]:<20}"
                f"{course[2]:<25}"
                f"{course[3]}\n"
            )
