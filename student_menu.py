from add_student import obj_add
from dispaly_student import obj_view_student_details
from search_student import Serach_student
from student_update import Obj_update_student_details
from delete import Obj_delete_student
from authorization import require_permission


class Student_Menu:
    def __init__(self):
        self.search = Serach_student()

    def Student_Menu(self):
        if not require_permission("student"):
            return

        while True:
            print("-"*50)
            print("\n*********** Welcome to Student Portal ***********\n")
            print("-"*50)
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Back to Previous Menu")
            print("-"*20)
                
            try:
                choice: int = int(input("Enter your choice[1-6]: "))
            except ValueError:
                print("Invalid choice! Please enter a number from 1 to 6.")
                continue
                
            if choice == 1:
                obj_add.add_student()
            elif choice == 2:
                obj_view_student_details.display_student()
            elif choice == 3:
                self.search.search_student()
            elif choice == 4:
                Obj_update_student_details.update_all()
            elif choice == 5:
                Obj_delete_student.delete_student()
            elif choice == 6:
                break
            else:
                print("Invalid choice! Please choose a number from 1 to 6.")
            
Obj_Student_menu = Student_Menu()


