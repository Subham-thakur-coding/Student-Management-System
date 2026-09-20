import sqlite3
import csv
import os
from db_config import Database
from validation import Validation
class StudentOperation:
    def __init__(self):
        self.db = Database()

    # Login logic
    def login(self, user_id, password):
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT * FROM user_auth
                    WHERE user_id = ? AND password = ?
                    """,(user_id, password))
        
        fetch = cursor.fetchone()
        
        con.close()
        
        if fetch:
            return True
        return False
    
    # Add Admin
    def add_admin(self, user_id, password):
        try:
            con : sqlite3.Connection = self.db.create_connection()
            cursor: sqlite3.Cursor = con.cursor()
            
            cursor.execute("SELECT user_id FROM user_auth WHERE user_id = ?", (user_id,))
            
            ex_user = cursor.fetchone()
            
            if ex_user:
                con.close()
                return False
            
            cursor.execute("""
                        INSERT INTO user_auth (user_id, password) VALUES (?, ?)
                        """, (user_id, password))
            con.commit()
            con.close()
            return True
        except sqlite3.Error as error:
            print(f"DATABASE error! {error}")
            # back-up if database error raise then it will run
            with open("admin_backup.csv", "a", newline="") as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(["user_id", "password"])
                writer.writerow([user_id, password])
                print("Admin details request saved in CSV file")
                print("\nAfter sometime it will be automatically  added in database when data base is active!. THANK YOU!")
                print("-"*40)
            return True

    # CSV to save data database
    def save_csv_to_database(self):

        filename = "admin_backup.csv"

    # Check CSV file exists
        if not os.path.exists(filename):
            print("\nNo CSV backup found.")
            return

        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                con: sqlite3.Connection = self.db.create_connection()
                with con:
                    cursor: sqlite3.Cursor = con.cursor()

                    for row in reader:
                        # Strip whitespace to support backups created with older headers.
                        values = {
                            (key or "").strip(): (value or "").strip()
                            for key, value in row.items()
                        }
                        cursor.execute("""
                            INSERT OR IGNORE INTO user_auth
                            (user_id, password)
                            VALUES (?, ?)
                        """, (
                            values["user_id"],
                            values["password"]
                        ))

                con.close()

            # Delete CSV after successful transfer
            os.remove(filename)

            print("\nCSV data successfully saved into database.")
            print("CSV backup file deleted.")

        except Exception as e:

            print("\nError while transferring CSV data to database:", e)

    # Remove Admin
    def remove_admin(self, user_id, password):
        try:
            con: sqlite3.Connection = self.db.create_connection()
            cursor: sqlite3.Cursor = con.cursor()
            cursor.execute("""
                        SELECT * FROM user_auth
                        WHERE user_id = ? AND password =?
                        """,(user_id, password))
            fetch = cursor.fetchone()
            if fetch is None:
                print("-"*50)
                print("Cridential Mismatch")
                print("-"*50)
                con.close()
                return False
            cursor.execute("""
                        DELETE FROM user_auth
                        WHERE user_id =? AND password=?
                        """,(user_id, password))
            con.commit()
            con.close()
            print("-"*50)
            print("\nAdmin Remove Successfully!")
            print("-"*50)
        except sqlite3.OperationalError as error:
            print(f"SomthinG went WRONG! TRY AGAIN ! {error}")

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
            
            # Add Admission
            cursor.execute("""
                        INSERT INTO student_admission
                        (student_id, admission_status)
                        VALUES(?, ?)
                        """,(student_id, admission))
            con.commit()
            print("\nStudent added successfully!")
            print("\n*********** ALERT ***********")
            print("You need to add course topic from main menu under the new course pannel!\n")
            print(f"New Student ID: {student_id}")
            print(f"Course ID: {course_id}")
        except sqlite3.OperationalError as error:
            con.close()
            print("-"*50)
            print(f"!!SOME OPERATIONAL ISSUE HAPPEN!! ERROR CODE:{error}")
            print("-"*50)