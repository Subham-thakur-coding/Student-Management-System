from db_config import Database
from operation import StudentOperation
from validation import Validation
from dispaly_student import Display_student
from search_student import Serach_student
from student_update import Update_student
from delete import Delete
class Menu:
    def __init__(self):
        self.db= Database()
        self.operation= StudentOperation()
        self.valid= Validation()
        self.display= Display_student()
        self.search= Serach_student()
        self.update= Update_student()
        self.delete= Delete()

    # Add admin
    def add_admin(self):
        
        print("\n========== ADD ADMIN ==========")

        while True:
            user_id: str = input("Enter user ID: ")
            if self.valid.validate_user_id(user_id):
                break
            else:
                print("Invalid User ID!")
                print("User ID must contain at least 4 alphabets and 2 digits.")
        while True:
            password: str = input("Enter Password: ")
            if self.valid.validate_password(password):
                break
            else:
                print("Invalid Password!")
                print("Password must contain at least 4 alphabets, 4 digits and 2 allowed special characters.")
        
        fetch = self.operation.add_admin(user_id, password)
        if fetch:
            self.operation.save_csv_to_database()
            print("\nAdmin created successfully!")
        else:
            print("\nERROR!")


    # Remove Admin
    def remove_admin(self):
        user_id :str = input("Enter User ID: ")
        password: str = input("Enter your Password:")

        fetch= self.operation.remove_admin(user_id, password)
        if fetch:
            print("-"*50)
            print(f"User ID: {user_id} remove successfully!")
            print("-"*50)

    # Login cridential
    def login(self):
        print("\n========== LOGIN ==========")
        while True:
            user_id: str = input("Enter user ID: ")
            print("-"*50)
            password: str = input("Enter password: ")
            print("-"*50)
            
            fetch = self.operation.login(user_id, password)
            
            if fetch:
                print("\nLogin Successful!")
                print(f"User ID: {user_id}")
                print("\nWelcome to Student Management System")
                return True
            else:
                print("\nInvalid User ID or Password!")
                print("-"*50)
                print("\n1. Try Again") 
                print("-"*50)
                print("2. Exit") 
                print("-"*50)
                choice: int = int(input("Enter your choice: "))
                
                if choice == 1:
                    continue
                elif choice == 2:
                    print("\nThank you!")
                    return False
                else:
                    print("Invalid choice!")
    # Pre Login Menu
    def pre_login(self):
        while True:
            print("\n")
            print("=" * 50)
            print(" STUDENT MANAGEMENT SYSTEM")
            print("=" * 50)
            print("1. Login")
            print("-"*50)
            print("2. Add Admin")
            print("-"*50)
            print("3. Remove Admin")
            print("-"*50)
            print("4. Exit")
            print("=" * 50)
            
            choice: int = int(input("Enter your choice: "))
            
            if choice == 1:
                login_success = self.login()
                if login_success:
                    self.main_menu()
            elif choice == 2:
                self.add_admin()
            elif choice == 3:
                self.remove_admin()
            elif choice == 4:
                print("\nThank you for using Student Management System!")
                break
            else:
                print("\nInvalid choice! Please choose 1-3.")
    # Main Menu
    def main_menu(self):
        print("\n")
        print("=" * 50)
        print(" MAIN MENU")
        print("=" * 50)
        print("1. Add Student")
        print("-"*50)
        print("2. Display Students")
        print("-"*50)
        print("3. Search Student") 
        print("-"*50)
        print("4. Update Student")
        print("-"*50)
        print("5. Delete Student") 
        print("-"*50)
        print("6. Exit")
        print("=" * 50) 
        choice: int = int(input("Enter your choice: ")) 
        if choice == 1:
            self.operation.add_student()
        elif choice == 2:
            self.display.display_student()
        elif choice == 3:
            self.search.search_student()
        elif choice == 4:
            self.update.update_details()
        elif choice == 5:
            self.delete.delete_student()
        else:
            print("*"*50)
            print("INVALID CHOICE!")
            print("*"*50)
    # After login part
    def start_program(self):
        self.db.create_table()
        self.operation.save_csv_to_database()
        self.pre_login()
if __name__ == "__main__":
    obj = Menu()
    obj.start_program()