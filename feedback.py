import csv

class Feedback_CSV:
    # Feddback logic when user opt for option number 4 from pre login menu
    def save_feedback(self):
        print("\n========== FEEDBACK ==========")

        feedback = input("Please write your experience or any suggestions for me: ")

        with open(
            "feedback.csv",
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            # Add heading if the file is empty
            if file.tell() == 0:
                writer.writerow(["Feedback : "])

            writer.writerow([feedback])

        print("\nThank you for your valuable feedback!")
        print("\n**************** We appreciate your time and effort in helping us improve our system. ****************")