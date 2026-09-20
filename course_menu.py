from display_course import Display_Course
from search_course import Search_Couse
from update_course_topic import Course_Topic
class Course_menu:
    def __init__(self) -> None:
        self.display= Display_Course()
        self.search= Search_Couse()
        self.topic= Course_Topic()
    # Menu
    def course_menu(self):
        
        while True:
            print("-"*50)
            print("\n*********** Welcome to course pannel ***********\n")
            print("-"*50)
            print("1. Dispaly Courses\n")
            print("2. Search Courses\n")
            print("3. Modify Courses Topics\n")
            print("4. Back to Main Menu\n")
            print("-"*20)
            
            choice: int = int(input("Enter your choice[1-4]: "))
            if choice == 1:
                self.display.display_course()
            elif choice == 2:
                self.search.search_course()
            elif choice == 3:
                self.topic.course_topic()
            elif choice == 4:
                break
            
            else:
                print("-"*20)
                print("Invalid choice. TRY AGAIN!")
                print("-"*20)
