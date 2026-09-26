import sqlite3
from validation import Validation
from db_config import Database
from autid_log import add_audit_log

class Add_student:
    def __init__(self):
        self.db = Database()
        
            # Add Student
    def add_student(self):
        print("\n========== ADD STUDENT ==========")
        
        # Name
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
                
        # Education
        while True:
            education: str = input("Enter Highest Qualification: ").upper()
            if Validation.validate_qualification(education):
                break
            else:
                print("Invalid qualification!")
        # Adress
        while True:
            adress: str = input("Enter student Address: ")
            if Validation.validate_address(adress):
                break
            else:
                print(f"Invalid Address![12/A, Lake Road]/ {adress}")
            
        # Course
        while True:
            course: str = input("Enter Course Name: ").capitalize()
            if Validation.validate_course(course):
                break
            else:
                print("Invalid course name!")
                
                
        # Course Duration
        while True:
            course_duration: str = input("Enter Course Duration (1-9 months): ")
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
                
        try:
            con: sqlite3.Connection = self.db.create_connection()
            cursor: sqlite3.Cursor = con.cursor()
            # Check whether course already exists
            cursor.execute("""
                        SELECT course_id
                        FROM student_course
                        WHERE course_name = ?
                        """,(course,))
            course_record = cursor.fetchone()
            if course_record:
                course_id = course_record[0]
            else:
                cursor.execute("""
                            INSERT INTO student_course(course_name, course_duration)
                            VALUES(?, ?)
                            """,(course, course_duration))
                course_id = cursor.lastrowid
                
            # Add Student
            cursor.execute("""
                        INSERT INTO student_details
                        (student_name, student_dob, student_adress, student_education, course_id)
                        VALUES (?, ?, ?, ?, ?)
                        """,(name,dob,adress,education,course_id))
            student_id = cursor.lastrowid
            # Add Payment Details
            cursor.execute("""
                        INSERT INTO payment_details
                        (student_id, amount, payment_status, paymnet_method, paymnet_datetime)
                        VALUES(?, ?, ?, ?, ?)
                        """,(student_id, 0.00, "PENDING", "PENDING", "No Activity"))
            # Add Admission
            cursor.execute("""
                        INSERT INTO student_admission
                        (student_id, admission_status)
                        VALUES(?, ?)
                        """,(student_id, admission))
            con.commit()
            add_audit_log("STUDENT ADDED",f"{student_id}, adeed into database")
            print("\nStudent added successfully!")
            print("\n*********** ALERT ***********")
            print("\n You need to add or update course topic, payment status and payment amount after successfully added student details!! \n")
            print("\n For course and payment related work refer to option 6 from main menu")
            print(f"New Student ID: {student_id}")
            print(f"Course ID: {course_id}")
        except sqlite3.OperationalError as error:
            con.close()
            
            print("-"*50)
            print(f"!!SOME OPERATIONAL ISSUE HAPPEN!! ERROR CODE:{error}")
            print("-"*50)
            
obj_add= Add_student()