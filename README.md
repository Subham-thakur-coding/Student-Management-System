# Student Management System

A menu-driven **Student Management System** built with **Python and SQLite**.
The project demonstrates practical use of **Object-Oriented Programming (OOP), SQLite database management, CSV file handling, validation, modular programming, and CRUD operations**.

## 🚀 Version 2.2 Beta

Version **2.2 Beta** extends the previous 2.0 Beta version with **Admission Management, Payment Database support, and Database-to-CSV export functionality**.

---

## ✨ Features

### 🔐 Admin Authentication

* Admin login system
* Add new admin credentials
* Password validation
* Secure access to the student management system

### 👨‍🎓 Student Management

* Add new students
* Display student details
* Search students
* Update student information
* Delete student records
* Automatic Student ID generation
* Course assignment for students

### 📚 Course Portal

* Display all available courses
* Search course by Course ID
* Add course topics
* Manage course-related information
* Automatic Course ID generation when required

### 🎓 Admission Management

Version 2.2 Beta introduces a dedicated **Admission & Payment Portal**.

Admission features include:

* Display all admission details
* Search admission information using Student ID
* Modify admission status
* Supported admission statuses:

  * Pending
  * Approved
  * Rejected

### 💳 Payment Database Support

A new `payment_details` table has been added to prepare the system for payment management.

The table stores:

* Payment ID
* Payment Status
* Payment Amount
* Student ID

The Payment module is currently under development and will be expanded in a future version.

### 📊 Export Database Tables to CSV

A new **Export Table to CSV** feature has been added.

The system:

1. Displays all available SQLite tables.
2. Allows the user to select a table.
3. Retrieves the table data.
4. Automatically creates a CSV file using the table name.
5. Exports column names and table records.
6. Prevents creation of a duplicate CSV file if the same file already exists.

For example:

```text
student_details → student_details.csv
student_course → student_course.csv
student_admission → student_admission.csv
payment_details → payment_details.csv
```

### 📝 Feedback System

When the user exits the application:

* A feedback form is displayed.
* User feedback is stored in a CSV file.
* CSV handling is implemented using a context manager.
* A feedback header is automatically added when the file is created.

### 🔮 Forgot Password

A **Forgot Password** option has been added to the main menu.

> Currently this feature is a placeholder and will be implemented in a future version.

---

## 🗄️ Database Structure

The application uses SQLite with the following main tables:

| Table               | Purpose                        |
| ------------------- | ------------------------------ |
| `user_auth`         | Stores admin login credentials |
| `student_course`    | Stores course information      |
| `student_details`   | Stores student information     |
| `student_admission` | Stores admission status        |
| `payment_details`   | Stores payment information     |

### Table Relationships

```text
student_course
      │
      │ course_id
      ▼
student_details
      │
      ├──────────────► student_admission
      │                  student_id
      │
      └──────────────► payment_details
                         student_id
```

---

## 📁 Project Structure

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
├── .gitignore
└── README.md
```

---

## 🆕 Changes from Version 2.0 Beta

### Version 2.2 Beta adds:

| Feature                       | Version 2.0 Beta | Version 2.2 Beta |
| ----------------------------- | ---------------- | ---------------- |
| Student Management            | ✅                | ✅                |
| Course Portal                 | ✅                | ✅                |
| Feedback System               | ✅                | ✅ Improved       |
| Admission Management          | ❌                | ✅                |
| Admission Status Modification | ❌                | ✅                |
| Payment Table                 | ❌                | ✅                |
| Payment Management            | ❌                | 🔄 Coming Soon   |
| Export SQLite Table to CSV    | ❌                | ✅                |
| Duplicate CSV Protection      | ❌                | ✅                |
| Admission & Payment Portal    | ❌                | ✅                |
| Forgot Password Option        | ❌                | 🔄 Coming Soon   |
| Course Panel renamed          | Panel            | Course Portal    |

---

## 🛠️ Technologies Used

* **Python 3**
* **SQLite3**
* **CSV**
* **Object-Oriented Programming**
* **Regular Expressions**
* **Context Managers**
* **Exception Handling**
* **CRUD Operations**
* **Modular Programming**

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd student_database_sqlite
```

### 3. Run the application

```bash
python main.py
```

The SQLite database and required tables are created automatically when the application initializes the database.

---

## 🔑 Default Admin Login

```text
User ID: admin
Password: admin123
```

You can add additional admin credentials through the application's admin option.

---

## 🎯 Learning Objectives

This project was developed as a practical Python project to strengthen understanding of:

* Python OOP
* Classes and objects
* SQLite database connectivity
* SQL queries
* Foreign keys
* CRUD operations
* Menu-driven applications
* Regular expression validation
* CSV file operations
* Context managers
* Exception handling
* Modular Python programming
* Database relationships
* Exporting database information to external files

---

## 🔮 Future Improvements

Planned features for upcoming versions include:

* Complete payment management
* Payment status updates
* Payment history
* Forgot Password functionality
* Improved input validation
* Better error handling
* Enhanced user interface
* Additional reports and data export options

---

## 📌 Project Status

**Version:** 2.2 Beta
**Status:** 🧪 Beta / Under Development

This project is continuously being improved as new Python, SQLite, OOP, and database concepts are learned and implemented.

---

## 👨‍💻 Author

**Subham Thakur**

Python Full Stack Development Learner
Interested in Python, Django, Web Development, Databases, and Generative AI.
