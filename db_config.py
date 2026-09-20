import sqlite3
# class for database creation
class Database:
    
    def create_connection(self) -> sqlite3.Connection:
        return sqlite3.connect("student_DB.db")

    def create_table(self):
        try:
            con: sqlite3.Connection = self.create_connection()
            cursour: sqlite3.Cursor = con.cursor()
            # 1. User auth table
            cursour.execute("""
                            CREATE TABLE IF NOT EXISTS user_auth(
                                user_id TEXT PRIMARY KEY NOT NULL,
                                password TEXT NOT NULL
                            ) 
                            """)
            # 2. Defult login details
            cursour.execute("""
                            INSERT OR IGNORE INTO user_auth(user_id, password)
                            VALUES(?,?)
                            """,("admin","admin123"))

            # 3. Student course details
            cursour.execute("""
                            CREATE TABLE IF NOT EXISTS student_course(
                                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                course_name TEXT NOT NULL,
                                course_duration TEXT NOT NULL,
                                course_topic TEXT
                            )
                            """)
            # 4. Student details table
            cursour.execute("""
                            CREATE TABLE IF NOT EXISTS student_details(
                                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                student_name TEXT NOT NULL,
                                student_dob TEXT NOT NULL,
                                student_adress TEXT NOT NULL,
                                student_education TEXT NOT NULL,
                                course_id INTEGER,
                                FOREIGN KEY(course_id) REFERENCES student_course(course_id)
                            )
                            """)
            
            # 5. Admission details
            cursour.execute("""
                            CREATE TABLE IF NOT EXISTS student_admission(
                                admission_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                student_id INTEGER NOT NULL,
                                admission_status TEXT NOT NULL,
                                FOREIGN KEY(student_id) REFERENCES student_details(student_id)
                            )
                            """)
            con.commit()
            con.close()
            print("-"*50)
            print("Connection Status with Database: ACTIVE")
            print("-"*50)
            
        except sqlite3.OperationalError as error:
            print(f"Try again! Database status: {error}")