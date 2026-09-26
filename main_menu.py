from authorization import has_permission, require_permission
from autid_log import add_audit_log, view_audit_logs
from user_session import UserSession
from student_menu import Obj_Student_menu
from course_menu import Obj_course_menu
from admission_menu import Obj_admision_menu
from payment_menu import Obj_payment_menu
from account_menu import Obj_account_menu
from feedback import Obj_feedback_CSV
class Main_Menu:
    def main_menu(self):

        while True:
                # dynamic menu basic on user role
            print("\n========== MAIN MENU ==========")

            if has_permission("student"):
                print("1. Student Management")

            if has_permission("course"):
                print("2. Course Management")

            if has_permission("admission"):
                print("3. Admission Management")

            if has_permission("payment"):
                print("4. Payment Management")

            if has_permission("account"):
                print("5. Account Management")

            if has_permission("audit"):
                print("6. Audit Logs")

            print("7. Logout")

            try:
                choice = int(input("\nEnter your choice: "))

            except ValueError:
                print("\nPlease enter a valid number.")

            # permission check
            if choice == 1:
                if not require_permission("student"):
                    continue
                Obj_Student_menu.Student_Menu()
            elif choice == 2:
                if not require_permission("course"):
                    continue
                Obj_course_menu.course_menu()
            elif choice == 3:
                if not require_permission("admission"):
                    continue
                Obj_admision_menu.admission_menu()
            elif choice == 4:
                if not require_permission("payment"):
                    continue
                Obj_payment_menu.payment_menu()
            elif choice == 5:
                if not require_permission("account"):
                    continue
                Obj_account_menu.account_menu()
            elif choice == 6:
                if not require_permission("audit"):
                    continue
                view_audit_logs()
            elif choice == 7:
                current_user = UserSession.get_user()
                add_audit_log(
                    "LOGOUT",
                    f"{current_user} logged out of the system"
                )
                UserSession.logout()
                Obj_feedback_CSV.save_feedback()
                print("\nLogout successfully!")
                break
            else:
                print("\nInvalid choice!")