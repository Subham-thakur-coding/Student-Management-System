import sqlite3
from db_config import Database
class Serach_student:
    def __init__(self):
        self.db= Database()
    # Searc Student details by id
    def search_student(self):
        student_id: int = int(input("Enter student's ID: "))
        
        con: sqlite3.Connection = self.db.create_connection()
        cousor: sqlite3.Cursor = con.cursor()
        
        cousor.execute("""
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
                    WHERE s.student_id =?
                    """,(student_id,))
        
        student_details = cousor.fetchone()
        
        if student_details is None:
            con.close()
            print("Details Not Found")
            return
        print("-"*50)
        print(f"Student Details Found for student's ID: {student_id}")
        print("-"*50)
        print(f"Student's Name: {student_details[1]}")
        print(f"Student's DOB(DD/MM/YYYY): {student_details[2]}")
        print(f"Student's Address: {student_details[3]}")
        print(f"Student's Education: {student_details[4]}")
        print(f"Student's Course: {student_details[5]}")
        print(f"Student's Course Duration: {student_details[6]}")
        print(f"Student's Admission Status: {student_details[7]}")