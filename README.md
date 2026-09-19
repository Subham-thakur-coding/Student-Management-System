# 🎓 Student Management System

A **Python-based Student Management System** built using **Object-Oriented Programming (OOP)** and **SQLite**. The project allows users to add, search, update, delete, and manage student information through a simple console-based interface.

The project also includes **CSV and JSON data handling**, input validation using **Regular Expressions**, and database operations using SQLite.

---

## 🚀 Features

* ➕ Add new student
* 🔍 Search student by ID
* ✏️ Update student details
* 🗑️ Delete student records
* 👤 Update personal student information
* 📚 Manage course information
* 📝 Manage admission status
* 💾 Store student data in SQLite database
* 📄 Work with CSV and JSON data
* 🔐 User ID and password validation
* ✅ Input validation using Regular Expressions
* 🧱 Object-Oriented Programming structure
* 🔗 Multiple database tables with relationships
* 📊 Retrieve student information using SQL `JOIN`

---

## 🛠️ Technologies Used

| Technology              | Purpose                                 |
| ----------------------- | --------------------------------------- |
| **Python**              | Main programming language               |
| **SQLite**              | Database management                     |
| **SQL**                 | Database queries                        |
| **OOP**                 | Project structure and code organization |
| **Regular Expressions** | Input validation                        |
| **CSV**                 | Import/export data                      |
| **JSON**                | Data storage and processing             |

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
├── db_config.py
├── validation.py
├── add_student.py
├── search_student.py
├── student_update.py
├── update_all_details.py
├── update_personal.py
├── delete_student.py
├── StudentJSON.py
├── StudentCSV.py
├── database/
│   └── student.db
│
├── README.md
└── requirements.txt
```

> The exact files may vary depending on the current version of the project.

---

## 🗄️ Database Structure

The project uses **SQLite** to store and manage student information.

### 1. `user_auth`

Stores user login and authentication information.

```text
user_auth
-------------------------
user_id
user_password
```

### 2. `student_course`

Stores information about the courses available to students.

```text
student_course
-------------------------
course_id
course_name
course_duration
```

### 3. `student_details`

Stores the main personal and educational information of students.

```text
student_details
-------------------------
student_id
student_name
dob
qualification
address
course_id
```

### 4. `student_admission`

Stores the admission status of students.

```text
student_admission
-------------------------
student_id
status
```

### 🔗 Table Relationships

The tables are connected using IDs:

```text
                    ┌─────────────────┐
                    │    user_auth    │
                    │    user_id      │
                    │  user_password  │
                    └─────────────────┘


┌──────────────────┐       ┌──────────────────┐
│ student_details  │       │ student_course   │
│                  │       │                  │
│ student_id       │       │ course_id        │
│ student_name     │       │ course_name      │
│ dob              │       │ course_duration  │
│ qualification    │       │                  │
│ address          │       └──────────────────┘
│ course_id ───────┼───────────────┐
└────────┬─────────┘                │
         │                          │
         │ student_id              │
         ↓                          │
┌──────────────────┐                │
│student_admission │                │
│                  │                │
│ student_id       │                │
│ status           │                │
└──────────────────┘                │
                                    │
                              course_id
```

The project uses SQL `JOIN` operations to retrieve related information from `student_details`, `student_course`, and `student_admission`.

For example:

```sql
SELECT
    s.student_id,
    s.student_name,
    s.dob,
    s.qualification,
    c.course_name,
    a.status
FROM student_details s
LEFT JOIN student_course c
    ON s.course_id = c.course_id
LEFT JOIN student_admission a
    ON s.student_id = a.student_id;
```


Stores admission information.

```text
student_admission
-------------------------
student_id
admission_status
```

The tables are connected using IDs and relationships.

For example:

```text
student_details
       |
       | course_id
       ↓
student_course

student_details
       |
       | student_id
       ↓
student_admission
```

---

## 🔄 Main Operations

### 1. Add Student

The application asks the user for:

* Student name
* Date of birth
* Address
* Highest qualification
* Course
* Course duration
* Admission status

Before inserting the data into the database, the input is validated.

Example:

```text
========== ADD STUDENT ==========

Enter student Name:
Enter Date of Birth (DD/MM/YYYY):
Enter Highest Qualification:
Enter student Address:
Enter Course Name:
Enter Course Duration:
Enter Admission Status:
```

After successful insertion:

```text
Student added successfully!
Student ID: 1
Course ID: 1
```

---

### 2. Search Student

Users can search for a student using the student's ID.

The application uses SQL `LEFT JOIN` to retrieve information from multiple tables.

Example:

```sql
SELECT
    s.student_id,
    s.student_name,
    s.student_dob,
    s.student_adress,
    s.student_education,
    c.course_name,
    c.course_duration,
    a.admission_status
FROM student_details s
LEFT JOIN student_course c
ON c.course_id = s.course_id
LEFT JOIN student_admission a
ON a.student_id = s.student_id
WHERE s.student_id = ?
```

The result displays the complete student information.

---

### 3. Update Student

The project provides two update options:

```text
1. Update all details
2. Update student's Personal Details
3. Exit
```

Users can update information such as:

* Name
* Date of birth
* Address
* Education
* Course
* Course duration
* Admission status

---

### 4. Delete Student

The delete functionality allows the user to remove a student record from the database using the student's ID.

---

## ✅ Input Validation

The project uses Python's `re` module for input validation.

For example, student names are checked using:

```python
pattern = r"^[A-Za-z ]+$"
```

This allows:

```text
Subham Thakur
Rahul Kumar
Amit
```

but rejects invalid input containing unwanted characters.

### Other Validations

The project validates:

* Student name
* Date of birth
* Qualification
* Course name
* Course duration
* Admission status
* Address
* User ID
* Password
* Yes/No inputs
* Menu options

---

## 📄 CSV & JSON Support

The project also works with external data formats such as:

### CSV

Student information can be read from a CSV file and processed by the application.

### JSON

Student information can also be handled using JSON.

Example JSON structure:

```json
{
    "student_name": "Subham Thakur",
    "dob": "01/01/2003",
    "qualification": "B.Com",
    "course": "Python"
}
```

This makes the project useful for learning how to move data between:

```text
User Input
    ↓
Python
    ↓
Dictionary / CSV / JSON
    ↓
SQLite Database
```

---

## 🧠 Concepts Used

This project was created to practice several important Python concepts.

### Python

* Variables
* Functions
* Loops
* Conditional statements
* Exception handling
* Modules
* File handling
* Type hints

### OOP

* Classes
* Objects
* Constructors
* Methods
* Encapsulation
* Multiple classes working together

### Database

* SQLite
* Connection
* Cursor
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `JOIN`
* Primary keys
* Foreign keys
* Transactions
* `commit()`
* `close()`

### Other Concepts

* Regular Expressions
* CSV handling
* JSON handling
* Context managers
* Data validation
* CRUD operations

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
```

### Step 2: Open the project

```bash
cd Student-Management-System
```

### Step 3: Run the application

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

---

## 💻 Example Menu

The application provides a menu-driven interface similar to:

```text
========================================
       STUDENT MANAGEMENT SYSTEM
========================================

1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Display Students
6. Exit

Enter your choice:
```

The available options may change as the project is developed.

---

## 🎯 Learning Objectives

The main purpose of this project is to understand how a real-world Python application can be connected to a database.

The project helped me practice:

```text
Python
   ↓
OOP
   ↓
Input Validation
   ↓
SQLite
   ↓
SQL Queries
   ↓
CRUD Operations
   ↓
CSV / JSON
```

It also demonstrates how multiple Python files/classes can work together as one application.

---

## 🔮 Future Improvements

Some possible improvements for future versions:

* 🌐 Convert the project into a web application using Django
* 🔐 Add a proper login and authentication system
* 👨‍💼 Add admin and user roles
* 🔎 Add advanced student search
* 📊 Add student statistics and reports
* 📤 Export database records to CSV/Excel
* 🖥️ Create a graphical user interface
* 🌐 Add REST API support
* 🤖 Add AI/Generative AI features
* ☁️ Connect the application to a cloud database

---

## 👨‍💻 Author

**Subham Thakur**

Python Full Stack Development Learner

### Skills Used in This Project

`Python` `OOP` `SQLite` `SQL` `Regex` `CSV` `JSON`

---

## ⭐ Project Status

🚧 **Currently under development**

The project is being continuously improved by adding new features, improving database operations, and practicing better Python programming techniques.

---

## 📜 License

This project is created for **learning and educational purposes**.
