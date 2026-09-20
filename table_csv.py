import csv
import os
import sqlite3
from db_config import Database
class Table_CSV:
    def __init__(self) -> None:
        self.db = Database()
    # logic for check table name
    def get_table_name(self):
        try:
            con: sqlite3.Connection = self.db.create_connection()
            cursor:sqlite3.Cursor = con.cursor()
            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type = 'table'
                AND name NOT LIKE 'sqlite_%'
            """)
            con.commit()
        except sqlite3.Error as e:
            con.close()
            print(f"Database Error {e}")

        tables = cursor.fetchall()
        return [table[0] for table in tables]
    def export_csv(self):
        tables = self.get_table_name()
        if not tables:
            print("No tables available.")
            return

        print("\n===== AVAILABLE TABLES =====")

        for number, table in enumerate(tables, start=1):
            print(f"{number}. {table}")

        try:
            choice = int(input("\nSelect table number: "))

            if choice < 1 or choice > len(tables):
                print("Invalid table selection.")
                return

            table_name = tables[choice - 1]

        except ValueError:
            print("Please enter a valid number.")
            return
        
        con: sqlite3.Connection = self.db.create_connection()
        cursor: sqlite3.Cursor = con.cursor()
        cursor.execute(f'SELECT * FROM "{table_name}"')
        rows = cursor.fetchall()

        column_names = [description[0] for description in cursor.description]

        file_name = f"{table_name}.csv"
        if os.path.exists(file_name):
            print(f"{file_name} already exists!\n")
            print("For updated data delete old file and retry!")
            print("CSV file not create!")
            return

        with open(file_name, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(column_names)
            writer.writerows(rows)
        print("-"*50)
        print(f"\nData successfully exported to {file_name}")
        print("-"*50)
