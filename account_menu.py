from forgot_password import Forgot_Password
from add_admin import Add_Admin
from authorization import require_permission
from modify_user_id import modify_user_id
class Account_Menu:
    def __init__(self) -> None:
        self.forgot_password = Forgot_Password()
        self.a_admin = Add_Admin()
    
    def account_menu(self):
        if not require_permission("account"):
            return
        while True:
            print("*"*50)
            print("\n*** Account & Database Configuration ***")
            print("*"*50)
            print("\n1. Add Admin")
            print("\n2. Change Admin User Id")
            print("\n3. Change Admin Password")
            print("\n4. Back to Previous Menu")
            
            choice: int = int(input("\nEnter your choice: "))
            if choice == 1:
                self.a_admin.add_admin()
            elif choice == 2:
                modify_user_id()
            elif choice == 3:
                self.forgot_password.forgot()
            elif choice == 4:
                break
            else:
                print("Invalid choice!")
                
Obj_account_menu = Account_Menu()