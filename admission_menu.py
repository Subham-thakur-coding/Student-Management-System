from display_admission import Display_admission
from modify_admission import Modify_admission
class Admission_Menu:
    def __init__(self) -> None:
        self.display= Display_admission()
        self.modify= Modify_admission()
    # logic for admission menu
    def admission_menu(self):
        while True:
            print("*"*50)
            print("\n---------------- Welcome to Admission Menu ----------------")
            print("*"*50)
            print("\n1. Display all admission details")
            print("\n2. Modify Admission Details")
            print("\n3. Back to Previous Menu")
            
            choice: int = int(input("\nEnter your choice: "))
            if choice == 1:
                self.display.display_admission()
            elif choice == 2:
                self.modify.update_status()
            elif choice == 3:
                break
            else:
                print("Invalid choice!")