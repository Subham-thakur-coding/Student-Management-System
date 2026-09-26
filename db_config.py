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
                                password TEXT NOT NULL,
                                user_role TEXT DEFAULT 'employee'
                            ) 
                            """)
            # Update user_auth table and add new field
            # cursour.execute("""
            #                 UPDATE user_auth
            #                 SET user_role = 'admin'
            #                 WHERE user_id = 'admin';
            #                 """)
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
                                student_status TEXT DEFAULT 'Pending',
                                FOREIGN KEY(course_id) REFERENCES student_course(course_id)
                            )
                            """)
            # Alter student_details table and add new field
            # cursour.execute("""
            #                 ALTER TABLE student_details
            #                 ADD COLUMN student_status TEXT DEFAULT 'Pending'
            #                 """)

            # 5. Admission details
            cursour.execute("""
                            CREATE TABLE IF NOT EXISTS student_admission(
                                admission_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                student_id INTEGER NOT NULL,
                                admission_status TEXT NOT NULL,
                                FOREIGN KEY(student_id) REFERENCES student_details(student_id)
                            )
                            """)
            # 6. Payment details
            cursour.execute("""
                            CREATE TABLE IF NOT EXISTS payment_details(
                                student_id INTEGER NOT NULL,
                                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                amount REAL,
                                payment_status TEXT,
                                paymnet_method TEXT DEFAULT 'Pending',
                                paymnet_datetime TEXT DEFAULT 'No Activity',
                                FOREIGN KEY (student_id) REFERENCES student_details(student_id)
                            )
                            """)
            # alter payment table
            # cursour.execute("""
            #                 ALTER TABLE payment_details
            #                 ADD COLUMN paymnet_method TEXT DEFULT 'Pending'
            #                 """)
            # cursour.execute("""
            #                 ALTER TABLE payment_details
            #                 ADD COLUMN paymnet_datetime TEXT DEFULT 'No Activity'
            #                 """)
            # 7. Audit Log
            cursour.execute("""
                CREATE TABLE IF NOT EXISTS audit_log (
                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    action TEXT NOT NULL,
                    description TEXT,
                    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            con.commit()

            
        except sqlite3.OperationalError as error:
            con.close()
            print("-"*50)
            print("\n***************Connection Status with Database: DISCONNECT!***************")
            print("-"*50)
            print(f"{error}")
            


# obj = Database()
# obj.create_table()