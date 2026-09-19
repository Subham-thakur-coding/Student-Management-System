import sqlite3
from db_config import Database
class Display_student:
    
    def __init__(self):
        self.db = Database()
    # Dispaly Student logic
    def display_student(self):
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT
                    s.student_id,
                    s.student_name,
                    s.student_dob,
                    s.student_adress,
                    s.student_education,
                    c.course_name,
                    c.course_duration,
                    a.admission_status
                    FROM student_details s
                    LEFT JOIN student_course c
                    ON c.course_id = s.course_id
                    LEFT JOIN student_admission a
                    ON a.student_id = s.student_id
                    """)
        
        students = cursor.fetchall()
        con.close()
        
        if not students:
            print("-"*50)
            print("!!\nNo Student Added, add student FIRST!!")
            print("-"*50)
            return False
        
        print("-" * 120)

        print(
            f"{'ID':<5}"
            f"{'Name':<10}"
            f"{'DOB':<15}"
            f"{'Address':<30}"
            f"{'Degree':<15}"
            f"{'Course':<20}"
            f"{'Duration':<10}"
            f"{'Status':<2}"
        )
        
        print("-" * 120)
        
        for student in students:
            student_id, name, dob, address, education, course, duration, status = student
            print(
                f"{student_id:<5}"
                f"{name:<10}"
                f"{dob:<15}"
                f"{address:<30}"
                f"{education:<15}"
                f"{course if course else 'N/A':<20}"
                f"{duration if duration else 'N/A':<12}"
                f"{status if status else 'N/A':<2}"
            )