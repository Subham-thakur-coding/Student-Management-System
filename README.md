# 🎓 Student Management System — Version 2.0

A **Python-based Student Management System** built using **Object-Oriented Programming (OOP)** and **SQLite**. The application provides a console-based interface for managing students, courses, and admission information.

Version 2.0 introduces a separate **Course Management Panel** and an **Exit Feedback System** using CSV and Python Context Managers.

---

## 🚀 Features

### 👨‍🎓 Student Management

* Add new students
* Display student records
* Search students by ID
* Update student information
* Delete student records
* Manage admission status

### 📚 Course Management Panel

A separate panel is available for course-related operations:

* Display all courses
* Search courses by Course ID
* Add course topics
* View course information

### 🔐 Authentication

* User authentication
* User ID and password validation
* Regular expression-based validation

### 💬 Exit Feedback

When the user exits the application:

1. A thank-you message is displayed.
2. The user is asked to provide feedback.
3. Feedback is stored in a CSV file.
4. A Python Context Manager is used for safe file handling.

### 💾 Data Management

* SQLite database
* CSV file handling
* JSON data handling
* SQL queries and joins
* Dictionary-based data processing

---

## 🛠️ Technologies Used

| Technology              | Purpose                 |
| ----------------------- | ----------------------- |
| **Python**              | Application development |
| **SQLite**              | Database management     |
| **SQL**                 | Database operations     |
| **OOP**                 | Code structure          |
| **Regular Expressions** | Input validation        |
| **CSV**                 | Feedback storage        |
| **JSON**                | Data processing         |
| **Context Manager**     | Safe file handling      |

---

## 🗄️ Database Structure

The project uses SQLite with the following main tables:

### `user_auth`

Stores authentication information.

### `student_details`

Stores student personal and educational information.

### `student_course`

Stores course information including:

* Course ID
* Course name
* Course duration
* Course topic

### `student_admission`

Stores student admission status.

The tables are related through `student_id` and `course_id`.

---

## 📚 Course Management

Version 2.0 separates course operations from the main student operations.

The Course Panel allows users to:

* Display all available courses
* Search for a course using its ID
* Add or update course topics
* View course details

This provides a dedicated area for managing course-related information.

---

## 💬 Feedback System

The application now collects user feedback when the program is closed.

Feedback is stored in a CSV file using Python's `csv` module.

A **Context Manager** is used to handle the file:

```python
with open("feedback.csv", "a", newline="") as file:
    # Store feedback
```

Using a context manager ensures that the file is automatically closed after the operation.

---

## ✅ Input Validation

The application uses **Regular Expressions (****`re`****)** and custom validation functions to validate user input.

Validation includes:

* Student name
* Date of birth
* Address
* Qualification
* Course name
* Course duration
* Course topic
* User ID
* Password
* Menu options
* Yes/No inputs

---

## 🧠 Concepts Practiced

### Python

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
* Modular programming

### SQLite & SQL

* Database connection
* CRUD operations
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `JOIN`
* Primary keys
* Foreign keys
* Transactions

### File Handling

* CSV
* JSON
* Context Managers

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
├── db_config.py
├── validation.py
│
├── StudentJSON.py
├── StudentCSV.py
│
├── database/
│   └── student.db
│
├── feedback/
│   └── feedback.csv
│
├── README.md
└── requirements.txt
```

> The exact file structure may vary depending on the current implementation.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
```

### 2. Open the project directory

```bash
cd Student-Management-System
```

### 3. Run the application

```bash
python main.py
```

---

## 🎯 Learning Objectives

This project was developed to practice building a real-world console application using Python and SQLite.

The project combines:

**Python → OOP → Validation → SQLite → SQL → CRUD → Course Management → CSV → Context Managers**

---

## 🔮 Future Improvements

* Convert the application into a Django web application
* Add Admin and User roles
* Improve authentication and authorization
* Add reports and analytics
* Export data to Excel
* Build a graphical user interface
* Create REST APIs
* Add AI/Generative AI features
* Connect to a cloud database

---

## 👨‍💻 Author

**Subham Thakur**

Python Full Stack Development Learner

**Technologies:**
`Python` `OOP` `SQLite` `SQL` `Regex` `CSV` `JSON`

---

## ⭐ Project Status

**Version 2.0 — Beta 👨‍💻**

The project is continuously improved as new Python, database, and software development concepts are learned and implemented.

---

## 📜 License

This project is created for **learning and educational purposes**.
