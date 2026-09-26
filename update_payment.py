import sqlite3
from datetime import datetime
from db_config import Database
from validation import Validation
from autid_log import add_audit_log
class Update_Payment:
    def __init__(self) -> None:
        self.db = Database()
        self.valid= Validation()
        
    # logic for update payment
    def update_payment(self):
        payment_id: int = int(input("\nEnter your payment id: "))
        con: sqlite3.Connection = self.db.create_connection()
        cousor: sqlite3.Cursor = con.cursor()
        
        cousor.execute("""
                    SELECT student_id,
                    payment_id,
                    amount,
                    payment_status,
                    paymnet_method,
                    paymnet_datetime
                    FROM payment_details
                    WHERE payment_id =?
                    """,(payment_id,))
        
        fetch: tuple = cousor.fetchone()
        
        if fetch is None:
            print("No payment details found")
            return False
        
        print("-"*20)
        print("**** Details Found ****")
        print("-"*20)
        print(f"Student ID: {fetch[0]}\n")
        print(f"Payment ID: {fetch[1]}\n")
        print(f"Amount: {fetch[2]}\n")
        print(f"Payment Status: {fetch[3]}\n")
        print(f"Payment Method: {fetch[4]}\n")
        print(f"Last activity Date and time: {fetch[5]}\n")
        # logic for update payment status
        while True:
            payment_status: str = input("Enter updated payment status[Pending/Approved/Rejected]: ").capitalize()
            if self.valid.validate_status(payment_status):
                break
            print("Invalid Status!")
        # logic for payment amount
        while True:
            amount = input("Enter Payment Amount: ")

            if self.valid.validate_payment_amount(amount):
                amount = float(amount)
                break
            else:
                print("Invalid payment amount!")
                print("Please enter a valid amount greater than 0.")
        # logic for update payment method
        while True:
            payment_method = input(
                "Enter Payment Method (Cash/UPI/Card/Net Banking): "
            ).strip().capitalize()

            if Validation.validate_payment_method(payment_method):
                payment_method = payment_method.title()
                break
            else:
                print("Invalid payment method!")
                print("Allowed: Cash, UPI, Card, Net Banking")
        # date time logic
        payment_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cousor.execute("""
                    UPDATE payment_details
                    SET amount =?,
                    payment_status =?,
                    paymnet_method =?,
                    paymnet_datetime =?
                    WHERE payment_id =?
                    """,(amount, payment_status, payment_method, payment_datetime, payment_id))
        con.commit()
        add_audit_log("PAYMENT DETAILS UPDATED",f"*** {payment_id}: payment ID, {payment_status}: paymnet status, {payment_method}: paymnet method, {payment_datetime}: Payment staus updated time **")
        print("\n*** ALERT ***")
        print(f"Payment ID: {payment_id} status updated successfully!")
        print(f"Current Payment Status: {payment_status}\n")
        try:
            con.close()
        except sqlite3.Error as e:
            print(f"Database Error : {e}")
# obj = Update_Payment()
# obj.update_payment()