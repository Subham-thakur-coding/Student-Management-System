from display_payment import Display_Payment
from update_payment import Update_Payment
from authorization import require_permission
class Payment_Menu:
    def __init__(self) -> None:
        self.d_payment = Display_Payment()
        self.u_payment = Update_Payment()
    # logic for payment menu
    def payment_menu(self):
        if not require_permission("payment"):
            return
        while True:
            print("*"*50)
            print("\n*** Welcome to Payment Portal ***")
            print("*"*50)
            print("\n1. Display Payment details")
            print("\n2. Modify Payment details")
            print("\n3. Back to Previous Menu")
            
            choice: int = int(input("\nEnter your choice: "))
            if choice == 1:
                self.d_payment.display_payment()
            elif choice == 2:
                self.u_payment.update_payment()
            elif choice == 3:
                break
            else:
                print("Invalid choice!")
                
Obj_payment_menu = Payment_Menu()