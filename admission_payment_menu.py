from admission_menu import Admission_Menu
class Admission_Payment_menu:
    def __init__(self) -> None:
        self.a_menu = Admission_Menu()
    # logic for admission and payment menu
    def menu(self):
        while True:
            print("*"*50)
            print("\n---------------- Welcome to Admission & Payment Portal ----------------")
            print("*"*50)
            print("\n1. Admission Work")
            print("\n2. Payment Work")
            print("\n3. Back to Main Menu")
            
            choice: int = int(input("\nEnter your choice: "))
            
            if choice == 1:
                self.a_menu.admission_menu()
            elif choice == 2:
                print("Comming soon!")
            elif choice == 3:
                break
            else:
                print("Invalid choice!")
