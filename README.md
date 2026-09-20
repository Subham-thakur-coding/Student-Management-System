# 🎓 Student Management System

A **menu-driven Student Management System** built using **Python and SQLite**.

This project demonstrates practical implementation of **Object-Oriented Programming, SQLite database management, CRUD operations, CSV handling, input validation, modular programming, context managers, and database relationships**.

---

# 🚀 Version 2.0 - Stable

**Status:** ✅ Stable Release
**Version:** `2.0 - Stable`
**Technology:** Python + SQLite
**Project Type:** Console-Based Database Application

Version 2.0 is the stable release of the second major development phase of the project.

This version includes **Student Management, Course Management, Admission Management, Payment Database Structure, Database-to-CSV Export, Admin Authentication, and Feedback Management**.

---

# ✨ Features

## 🔐 Admin Authentication

The system provides an authentication system for administrators.

Features include:

* Admin Login
* Add Admin
* Login Validation
* Default Admin Account
* Admin Data Handling

---

# 👨‍🎓 Student Management

The core Student Management functionality includes:

* Add Student
* Display Student
* Search Student
* Update Student
* Delete Student
* Automatic Student ID generation
* Student course assignment
* Automatic admission record creation

Student information includes:

* Student ID
* Student Name
* Date of Birth
* Student Address
* Student Education
* Course ID

---

# 📚 Course Portal

The **Course Portal** provides course-related management functionality.

### Available Options

* Display Courses
* Search Course
* Update Course Topic
* Return to Main Menu

Course information includes:

* Course ID
* Course Name
* Course Duration
* Course Topic

The Course ID connects `student_details` with `student_course`.

---

# 🎓 Admission / Payment Portal

The application contains a separate **Admission / Payment Portal**.

```text
Admission / Payment Portal
│
├── 1. Admission Work
│   ├── Display All Admission Details
│   └── Modify Admission Details
│
├── 2. Payment Work
│   └── Coming Soon
│
└── 3. Back to Main Menu
```

## Admission Work

The Admission Work section provides:

* Display All Admission Details
* Modify Admission Details
* Update Admission Status

Supported admission statuses:

```text
Pending
Approved
Rejected
```

---

# 💳 Payment Details

Version 2.0 introduces a new **`payment_details`** table to prepare the application for future payment management.

### `payment_details`

| Column           | Description        |
| ---------------- | ------------------ |
| `payment_id`     | Unique Payment ID  |
| `payment_status` | Payment status     |
| `amount`         | Payment amount     |
| `student_id`     | Related Student ID |

The **Payment Work** option is currently reserved for future development.

---

# 📊 Export Table to CSV

The **Export Table to CSV** feature allows database table information to be exported into CSV files.

### Process

1. Select **Export Table to CSV** from the Main Menu.
2. The application displays the available database tables.
3. Select the required table.
4. The selected table data is exported to a CSV file.
5. Column names are included automatically.
6. If the CSV file already exists, the application does not overwrite it.

### Available Database Tables

```text
1. user_auth
2. student_course
3. student_details
4. student_admission
5. payment_details
```

Example exports:

```text
user_auth → user_auth.csv
student_course → student_course.csv
student_details → student_details.csv
student_admission → student_admission.csv
payment_details → payment_details.csv
```

---

# 📝 Feedback System

The application provides a feedback option when the user chooses to exit the program.

The feedback system:

* Accepts user feedback
* Stores feedback in `feedback.csv`
* Uses CSV file handling
* Uses a context manager for file operations
* Adds the CSV header when required

Example:

```text
Feedback :
System is easy to use.
```

> `feedback.csv` is a CSV file and is **not a SQLite database table**.

---

# 🔑 Forgot Password

The Main Menu includes:

```text
9. Forgot Password
```

The current functionality displays:

```text
Coming Soon!
```

This feature is reserved for future authentication improvements.

---

# 🗄️ Database Structure

The application uses **SQLite** as its database.

## Database Tables

| Table Name          | Purpose                                |
| ------------------- | -------------------------------------- |
| `user_auth`         | Stores administrator login credentials |
| `student_course`    | Stores course information              |
| `student_details`   | Stores student information             |
| `student_admission` | Stores admission information           |
| `payment_details`   | Stores payment information             |

---

## 🔗 Database Relationships

```text
┌────────────────────┐
│   student_course   │
│                    │
│ course_id (PK)     │
│ course_name        │
│ course_duration    │
│ course_topic       │
└─────────┬──────────┘
          │
          │ course_id
          ▼
┌────────────────────┐
│   student_details  │
│                    │
│ student_id (PK)    │
│ student_name       │
│ student_dob        │
│ student_adress     │
│ student_education  │
│ course_id (FK)     │
└─────────┬──────────┘
          │
     ┌────┴─────┐
     │          │
     ▼          ▼
┌────────────┐  ┌─────────────────┐
│ student_   │  │ payment_details │
│ admission  │  │                 │
│            │  │ payment_id (PK) │
│ admission_ │  │ student_id (FK) │
│ id (PK)    │  │ payment_status  │
│ student_id │  │ amount          │
│ (FK)       │  └─────────────────┘
│ admission_ │
│ status     │
└────────────┘
```

### Foreign Key Relationships

* `student_details.course_id` → `student_course.course_id`
* `student_admission.student_id` → `student_details.student_id`
* `payment_details.student_id` → `student_details.student_id`

---

# 📁 Project Structure

```text
student_database_sqlite/
│
├── main.py
├── db_config.py
├── operation.py
├── validation.py
│
├── dispaly_student.py
├── search_student.py
├── student_update.py
├── update_personal.py
├── update_all_details.py
├── delete.py
│
├── course_menu.py
├── display_course.py
├── search_course.py
├── update_course_topic.py
│
├── admission_payment_menu.py
├── admission_menu.py
├── display_admission.py
├── modify_admission.py
│
├── table_csv.py
├── feedback.py
│
├── student_DB.db
├── feedback.csv
├── student_details.csv
│
├── .gitignore
└── README.md
```

---

# 🛠️ Technologies Used

* **Python 3**
* **SQLite3**
* **CSV**
* **Object-Oriented Programming**
* **Regular Expressions**
* **Context Managers**
* **Exception Handling**
* **CRUD Operations**
* **File Handling**
* **SQL**
* **Foreign Keys**
* **Modular Programming**

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Open the Project

```bash
cd student_database_sqlite
```

## 3. Run the Application

```bash
python main.py
```

The application creates the required SQLite database tables when the database is initialized.

---

# 🔑 Default Admin Account

The application provides a default administrator account:

```text
User ID: admin
Password: admin123
```

---

# 📋 Main Menu

The Version 2.0 Stable application contains:

```text
==================================================
                    MAIN MENU
==================================================

1. Add Student
2. Display Student
3. Search Student
4. Update Student
5. Delete Student
6. Course Portal
7. Admission / Payment Portal
8. Export Table to CSV
9. Forgot Password
10. Log out
```

---

# 📚 Course Portal Menu

```text
--------------------------------------------------
                  Course Portal
--------------------------------------------------

1. Display Courses
2. Search Course
3. Update Course Topic
4. Back to Main Menu
```

---

# 🎓 Admission / Payment Portal Menu

```text
--------------------------------------------------
          Admission / Payment Portal
--------------------------------------------------

1. Admission Work
2. Payment Work
3. Back to Main Menu
```

### Admission Menu

```text
--------------------------------------------------
                 Admission Menu
--------------------------------------------------

1. Display All Admission Details
2. Modify Admission Details
3. Back to Previous Menu
```

---

# 🎯 Learning Objectives

This project was created as a practical Python project to understand how a database-driven application can be developed.

The project demonstrates:

* Python Classes and Objects
* Object-Oriented Programming
* SQLite Database Connectivity
* SQL Queries
* Database Tables
* Primary Keys
* Foreign Keys
* Database Relationships
* CRUD Operations
* Input Validation
* Regular Expressions
* CSV File Handling
* Context Managers
* Exception Handling
* Modular Programming
* Database-to-CSV Export
* Menu-Driven Application Development

---

# 🔄 Version 2.0 Highlights

### Added

* ✅ Course Portal
* ✅ Course Search
* ✅ Course Topic Management
* ✅ Admission Management
* ✅ Admission Status Modification
* ✅ Admission / Payment Portal
* ✅ `payment_details` Table
* ✅ Export Table to CSV
* ✅ Database Table Selection
* ✅ Duplicate CSV Protection
* ✅ Feedback CSV System
* ✅ Context Manager for Feedback
* ✅ Forgot Password Menu Option

### Maintained

* ✅ Student CRUD Operations
* ✅ Admin Authentication
* ✅ Student Validation
* ✅ SQLite Database
* ✅ Course Assignment
* ✅ Modular Project Structure

---

# 📌 Project Status

## ✅ Version 2.0 - Stable

Version 2.0 is the **stable release of Version 2**.

The core Student Management functionality, Course Portal, Admission Management, database structure, CSV export functionality, and feedback system are implemented.

Some options, such as **Payment Work** and **Forgot Password**, are reserved for future development.

---

# 🔮 Future Development

Future versions may include:

* Complete Payment Management
* Payment Processing
* Payment History
* Payment Status Management
* Forgot Password Functionality
* Password Reset System
* Improved Authentication
* Additional Reports
* Improved Validation
* Enhanced Error Handling
* Additional Database Features

---

# 👨‍💻 Author

**Subham Thakur**

Python Full Stack Development Learner

### Interests

* Python
* Django
* SQLite
* Web Development
* Generative AI
* Software Development

---

# 📜 Version History

| Version            | Status       | Major Changes                         |
| ------------------ | ------------ | ------------------------------------- |
| `1.x`              | Previous     | Basic Student Management System       |
| `2.0 Beta`         | Previous     | Course Portal and Feedback System     |
| **`2.0 - Stable`** | **✅ Stable** | **Final Stable Release of Version 2** |

---

## 🎉 Version 2.0 - Stable

**Student Management System — Stable Release**

> Built with Python, SQLite, OOP, and continuous learning.
