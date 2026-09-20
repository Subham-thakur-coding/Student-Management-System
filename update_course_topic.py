import sqlite3
from db_config import Database
from validation import Validation

class Course_Topic:
    def __init__(self) -> None:
        self.db= Database()
        self.valid = Validation()
        
    # Logic for topic course details
    def course_topic(self):
        course_id: int = int(input("\nEnter your course ID: "))
        
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT
                    course_name,
                    course_duration,
                    course_topic
                    FROM student_course
                    WHERE course_id =?
                    """, (course_id,))
        
        fetch = cursor.fetchone()
        
        if fetch is None:
            print("-"*50)
            print(f"Course details not or course not added! ID: {course_id}")
            print("-"*50)
            return False
        
        print("-"*20)
        print("*********** Details Found ***********")
        print("-"*20)
        print(f"Course Name: {fetch[0]}\n")
        print(f"Course Duration: {fetch[1]}\n")
        print(f"Course Topic: {fetch[2]}\n")
        
        while True:
            course_topic: str = input("Add course topic:  ")
            if self.valid.validate_course_topic(course_topic):
                break
            print("Invalid course topic!")
            
        cursor.execute("""
                    UPDATE student_course
                    SET course_topic =?
                    WHERE course_id =?
                    """,(course_topic, course_id))
        try:
            con.commit()
            print("\nChanges saved successfully!")
        except sqlite3.Error as e:
            con.close()
            print(f"Database Error {e}")