import sqlite3
from db_config import Database
from validation import Validation

class Update_all_Details:
    def __init__(self):
        self.db = Database()
        self.valid = Validation()
    # Logic for update student's all details
    def update_all(self):
        student_id: int = int(input("Enter Student's ID: "))
        
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
                    WHERE s.student_id =?
                    """,(student_id,))
        response = cursor.fetchone()
        
        if not response:
            print("No Student Details Found!")
            con.close()
            return
        print(f"\nStudent's Details Found for this ID: {student_id}")
        print("-"*30)
        print("\tOld Data")
        print("-"*30)
        print(f"Student's Name: {response[1]}")
        print(f"Student's DOB(DD/MM/YYYY): {response[2]}")
        print(f"Student's Address: {response[3]}")
        print(f"Student's Education: {response[4]}")
        print(f"Student's Course: {response[5]}")
        print(f"Student's Course Duration: {response[6]}")
        print(f"Student's Admission Status: {response[7]}")
        print("-"*40)
        print("Enter New Data Below")
        while True:
            name: str = input("Enter student Name: ").capitalize()
            if Validation.validate_name(name):
                break
            else:
                print("Invalid name! Please enter alphabets only.")
        # DOB
        while True:
            dob: str = input("Enter Date of Birth (DD/MM/YYYY): ")
            if Validation.validate_dob(dob):
                break
            else:
                print(f"Invalid date format![DD/MM/YYYY]/{dob} ")
                
        # Adress
        while True:
            adress: str = input("Enter student Address: ")
            if Validation.validate_address(adress):
                break
            else:
                print(f"Invalid Address![12/A, Lake Road]/ {adress}")

        # Education
        while True:
            education: str = input("Enter Highest Qualification: ").upper()
            if Validation.validate_qualification(education):
                break
            else:
                print("Invalid qualification!")

            
        # Course
        while True:
            course: str = input("Enter Course Name: ").capitalize()
            if Validation.validate_course(course):
                break
            else:
                print("Invalid course name!")
                
                
        # Course Duration
        while True:
            course_duration: str = input("Enter Course Duration: ")
            if Validation.validate_course_duration(course_duration):
                break
            else:
                print("Invalid Course Duration!")
        
        # Admission
        while True:
            admission: str = input("Enter Admission Status (Pending/Approved/Rejected): ").capitalize()
            if Validation.validate_status(admission):
                break
            else:
                print("Invalid status!")
        # check course status
        cursor.execute("""
                    SELECT course_id
                    FROM student_course
                    WHERE course_name = ?
                    """, (course,))
        course_record = cursor.fetchone()

        if course_record:
            course_id = course_record[0]
        else:
            cursor.execute("""
                        INSERT INTO student_course (course_name, course_duration)
                        VALUES (?, ?)
                        """, (course, course_duration))
            course_id = cursor.lastrowid

        # Update Student
        cursor.execute("""
            UPDATE student_details
            SET student_name = ?,
                student_dob = ?,
                student_adress = ?,
                student_education = ?,
                course_id = ?
            WHERE student_id = ?
        """, (
            name,
            dob,
            adress,
            education,
            course_id,
            student_id
        ))

        # Update Admission
        cursor.execute("""
                    SELECT 1
                    FROM student_admission
                    WHERE student_id = ?
                    """, (student_id,))
        admission_record = cursor.fetchone()

        if admission_record:
            cursor.execute("""
                        UPDATE student_admission
                        SET admission_status = ?
                        WHERE student_id = ?
                        """, (admission, student_id))
        else:
            cursor.execute("""
                        INSERT INTO student_admission (student_id, admission_status)
                        VALUES (?, ?)
                        """, (student_id, admission))

        try:
            con.commit()

            print("="*50)
            print("\n\tUPDATE Done!")
            print("="*50)
        except sqlite3.Error as error:
            con.close()
            print(f"Check your code error is {error}")