import sqlite3
from db_config import Database
from validation import Validation

class Update_Personal_Details:
    def __init__(self):
        self.db = Database()
        self.valid = Validation()
    # Logic for update student's personal details
    def update_personal(self):
        student_id: int = int(input("Enter Student's ID: "))
        
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        
        cursor.execute("""
                    SELECT
                    student_id,
                    student_name,
                    student_dob,
                    student_adress,
                    student_education
                    FROM student_details
                    WHERE student_id =?
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
        cursor.execute("""
                    UPDATE student_details
                    SET student_name =?,
                    student_dob =?,
                    student_adress =?,
                    student_education=?
                    """,(name, dob, adress, education))
        try:
            con.commit()
            print("-"*30)
            print("Student Personal details update successfully!")
            print("-"*30)
        except sqlite3.Error as error:
            con.close()
            print(f"Check your code error is {error}")