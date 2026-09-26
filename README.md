# 🎓 Student Management System

> **A modular, role-aware, database-driven Student Management System built with Python, OOP and SQLite.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Version](https://img.shields.io/badge/Version-3.0.0%20Beta-orange?style=for-the-badge)](#-version-300-beta)
[![Status](https://img.shields.io/badge/Status-Active%20Development-2ea44f?style=for-the-badge)](#-roadmap)

---

## ✨ What is this project?

This project started as a simple **Python + SQLite student CRUD application** and gradually evolved into a more structured console-based management system.

The goal is not only to store student data, but to simulate how different departments can work with the same database while following controlled access, validation, auditing and modular workflows.

### 🧭 Project evolution

```text
Simple CRUD
    ↓
Authentication + Validation
    ↓
Course Management
    ↓
Feedback + File Handling
    ↓
Role-Based Access Control
    ↓
Payment Management
    ↓
Account Management
    ↓
Audit Logging
    ↓
3.0.0 Beta — Multi-module Management System
    ↓
Future: Workflow / Queue / External User Interface
```

---

# 🚀 Current Release — v3.0.0 Beta

**3.0.0 Beta is the point where the project moves beyond a basic student CRUD program and starts behaving like a small role-based management application.**

### 🔥 Major additions in 3.0.0 Beta

| Area | 2.0.0 Stable | 3.0.0 Beta |
|---|---|---|
| Student CRUD | ✅ | ✅ |
| Course management | ✅ | ✅ |
| Authentication | ✅ | ✅ |
| Input validation | ✅ | ✅ |
| Feedback CSV | ✅ | ✅ |
| Payment management | Basic database support | 🆕 Dedicated Payment Portal |
| User roles | ❌ | 🆕 Admin / Employee |
| Authorization | ❌ | 🆕 Permission-based access |
| User session | ❌ | 🆕 Centralized session state |
| Audit log | ❌ | 🆕 Login / logout / data activity tracking |
| Account management | ❌ | 🆕 Admin account controls |
| Password change | ❌ | 🆕 Forgot/change password workflow |
| User ID change | ❌ | 🆕 Account identifier modification |
| Admin/user creation | Basic authentication setup | 🆕 Role-aware account creation |
| Dynamic main menu | ❌ | 🆕 Menu changes according to role |
| Modular portals | Partial | 🆕 Student / Course / Admission / Payment / Account / Audit |
| Database model | Multi-table | Expanded with audit + role data |

---

# 🕰️ The Story of the Project

This section documents **how the project grew version by version**, so a viewer can understand the development journey instead of seeing only the latest code.

## 🌱 Version 1 — The Foundation

The project began as a learning-focused Student Management System.

### Core goal
Build a working application using:

- Python
- Functions
- OOP
- SQLite
- SQL CRUD operations
- Input validation

### Main capabilities

- Add students
- Display students
- Search students
- Update students
- Delete students
- Store data in SQLite
- Validate user input
- Create relationships between student and course/admission data

**Focus:** Learn the fundamentals of connecting Python with a relational database.

---

## 📘 Version 2.0 Beta — Better Structure

The second generation focused on expanding the original CRUD application.

### Major changes

- Introduced a dedicated **Course Management Panel**
- Added course searching
- Added course topic management
- Improved student/course database relationships
- Expanded validation
- Improved modularity
- Added more structured database operations

**Focus:** Move from a simple CRUD script toward a multi-module application.

---

## 🧪 Version 2.2 Beta — Feature Expansion

The project continued to evolve with additional database and usability features.

### Highlights

- Expanded admission-related operations
- Improved course handling
- Added payment-related database support
- Added feedback collection
- Improved CSV/file handling
- Continued refactoring and bug fixing

**Focus:** Make the application represent more realistic student-management operations.

---

## 🏁 Version 2.0.0 Stable — The Stable Baseline

The stable 2.0 generation established the foundation used by the next major version.

### Stable capabilities

- Student Management
- Course Management
- Admission Management
- Authentication
- SQLite database
- SQL CRUD operations
- Input validation
- CSV feedback storage
- Context-manager based file handling
- Modular Python files

At this stage, the application was primarily a **data-management system**.

### The limitation that led to v3

Although the application had multiple modules, access control was not yet separated by user role.

The next logical step was to answer:

> **Who is allowed to do what?**

That question became the foundation of Version 3.

---

# 🧠 Version 3.0.0 Beta — From CRUD to Controlled Access

Version 3 introduces an important architectural change:

```text
              ┌─────────────────────┐
              │    Authentication   │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │    User Session     │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Authorization Layer │
              └──────────┬──────────┘
                         ↓
       ┌─────────┬────────┼─────────┬──────────┐
       ↓         ↓        ↓         ↓          ↓
    Student   Course   Admission  Payment   Account
       │         │        │         │          │
       └─────────┴────────┴─────────┴──────────┘
                         ↓
                 SQLite Database
                         ↓
                    Audit Logs
```

---

# 🔐 Role-Based Access Control

The application now contains a dedicated authorization layer.

### 👑 Admin

The current authorization configuration gives the **admin** access to:

- Student Management
- Course Management
- Admission Management
- Payment Management
- Account Management
- Audit Logs

### 👤 Employee

The current authorization configuration gives an **employee** access to:

- Student Management
- Course Management

This is implemented through a centralized permission map rather than scattering role checks throughout every operation.

```python
PERMISSIONS = {
    "admin": {
        "student",
        "course",
        "admission",
        "payment",
        "account",
        "audit"
    },

    "employee": {
        "student",
        "course"
    }
}
```

---

# 🧩 Modular Portal Architecture

The main menu now behaves according to the logged-in user's role.

### 🧑‍🎓 Student Portal

- Add student
- Display students
- Search student
- Update student
- Delete student

### 📚 Course Portal

- Display courses
- Search courses
- Modify course topics

### 📝 Admission Portal

- Display admission details
- Modify admission status

### 💳 Payment Portal

- Display payment records
- Modify payment details
- Validate payment status
- Validate amount
- Validate payment method
- Automatically record payment date/time

### ⚙️ Account Portal

- Add user/admin account
- Change user ID
- Change password

### 🧾 Audit Portal

- View recorded system activities
- Track user
- Track action
- Track description
- Track timestamp

---

# 🧾 Audit Logging

Version 3 introduces a dedicated `audit_log` table.

```text
audit_log
├── log_id
├── user_id
├── action
├── description
└── log_time
```

The system records activities such as:

- Login
- Logout
- Student creation
- Payment updates
- Admission updates
- Password changes
- Account-related operations
- Data viewing activities implemented by the modules

This creates a basic activity trail for the application.

---

# 👤 User Session Management

Version 3 introduces a centralized `UserSession` class.

The session keeps track of:

```text
Current User
Current Role
```

This information is then used by the authorization layer to determine which modules the current user can access.

---

# 💳 Payment Management

Payment functionality is now exposed through its own portal.

Payment records contain:

- Student ID
- Payment ID
- Amount
- Payment status
- Payment method
- Payment date/time

Supported payment methods are validated by the application, including:

- Cash
- UPI
- Card
- Net Banking

Payment activity automatically records the current date and time.

---

# 🔑 Account & Password Management

The Account Portal introduces administrative account operations.

### Available operations

- Add user account
- Change user ID
- Change password
- Validate account credentials
- Record account activity in audit logs

The password-change workflow also checks:

- User ID
- Password format
- Confirmation password
- Final confirmation before database update

---

# 🗄️ Database Architecture

The current database is built around multiple related SQLite tables.

```text
┌────────────────────┐
│     user_auth      │
│ user_id            │
│ password           │
│ user_role          │
└─────────┬──────────┘
          │
          │ session / authorization
          ↓
┌────────────────────┐
│  student_details   │
│ student_id         │
│ student_name       │
│ DOB                │
│ address            │
│ education          │
│ course_id          │
│ student_status     │
└─────────┬──────────┘
          │
     ┌────┴───────────────┐
     ↓                    ↓
┌───────────────┐   ┌──────────────────┐
│ student_course│   │student_admission │
│ course_id     │   │ admission_id     │
│ course_name   │   │ student_id       │
│ duration      │   │ status           │
│ topic         │   └──────────────────┘
└───────────────┘
          │
          ↓
┌──────────────────┐
│ payment_details  │
│ student_id       │
│ payment_id       │
│ amount           │
│ status           │
│ method           │
│ date/time        │
└──────────────────┘

┌──────────────────┐
│    audit_log     │
│ log_id           │
│ user_id          │
│ action           │
│ description      │
│ timestamp        │
└──────────────────┘
```

---

# 🛡️ Validation Layer

Input validation remains an important part of the application.

The validation module handles fields such as:

- Student name
- Date of birth
- Address
- Qualification
- Course name
- Course duration
- Course topic
- User ID
- Password
- Status
- Payment amount
- Payment method
- Menu choices

Regular expressions and dedicated validation functions are used to keep invalid input away from the database operations.

---

# 🧱 Project Architecture

The project is intentionally divided into smaller modules instead of placing the entire application inside one Python file.

```text
student_database_sqlite/
│
├── main.py
├── main_menu.py
├── db_config.py
├── validation.py
│
├── authorization.py
├── user_session.py
├── autid_log.py
│
├── student_menu.py
├── add_student.py
├── student_update.py
├── search_student.py
├── dispaly_student.py
├── delete.py
│
├── course_menu.py
├── display_course.py
├── search_course.py
├── update_course_topic.py
│
├── admission_menu.py
├── display_admission.py
├── modify_admission.py
│
├── payment_menu.py
├── display_payment.py
├── update_payment.py
│
├── account_menu.py
├── add_admin.py
├── modify_user_id.py
├── forgot_password.py
│
├── feedback.py
├── feedback.csv
├── student_details.csv
│
└── README.md
```

> File names reflect the current 3.0.0 beta implementation.

---

# 🛠️ Technology Stack

| Technology | Used For |
|---|---|
| 🐍 **Python** | Core application |
| 🗃️ **SQLite** | Database |
| 🔎 **SQL** | CRUD, relationships and queries |
| 🧱 **OOP** | Modular application design |
| 🔐 **Authorization** | Role-based permissions |
| 👤 **Session Management** | Current user/role state |
| 🧾 **Audit Logging** | Activity tracking |
| 🧪 **Regex / Validation** | Input validation |
| 📄 **CSV** | Feedback and data handling |
| 🕒 **datetime** | Payment activity timestamps |

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
```

### 2. Open the project

```bash
cd Student-Management-System
```

### 3. Run the application

```bash
python main.py
```

The application will create/use the SQLite database and initialize the required tables.

---

# 🔑 Default Login

The current database initialization contains a default account:

```text
User ID  : admin
Password : admin123
```

> ⚠️ This credential is intended for local development/learning. Change it before using the project in any real environment.

---

# 🧪 Version Comparison

## 2.0.0 Stable → 3.0.0 Beta

### Architecture

**2.0.0**

```text
Main Program
     ↓
Student / Course / Admission
     ↓
SQLite
```

**3.0.0 Beta**

```text
Authentication
      ↓
User Session
      ↓
Authorization
      ↓
Role-based Modules
      ↓
SQLite
      ↓
Audit Trail
```

### What changed?

**2.0.0 was mainly about managing data.**

**3.0.0 Beta adds control around that data.**

That means the project moved from:

> **“Can the application store and modify student information?”**

toward:

> **“Which user can access which part of the application, and what activity happened?”**

That architectural shift is the main story of the 3.0.0 release.

---

# 📈 Development Progress

```text
Version 1
│
├── Python fundamentals
├── SQLite
├── CRUD
└── Validation
        │
        ▼
Version 2.0
│
├── Course Management
├── Admission Management
├── Feedback
├── CSV / Context Manager
└── Better modular structure
        │
        ▼
Version 2.2 Beta
│
├── Feature expansion
├── Payment support
├── Database improvements
└── Workflow improvements
        │
        ▼
Version 2.0.0 Stable
│
└── Stable multi-module baseline
        │
        ▼
Version 3.0.0 Beta
│
├── RBAC
├── User Sessions
├── Permission Layer
├── Audit Logs
├── Payment Portal
├── Account Portal
├── Password Management
└── Dynamic Role-Based Menu
        │
        ▼
Future
│
├── Queue / workflow engine
├── External student interaction
├── Telegram integration
├── Better security
├── Reporting / analytics
├── Django web version
└── AI-assisted features
```

---

# 🔮 Roadmap

The project is still evolving.

Possible future directions include:

- [ ] Improve password security with hashing
- [ ] Strengthen authentication and authorization
- [ ] Add more granular department permissions
- [ ] Introduce a proper admission → payment → faculty workflow
- [ ] Add queue-based processing
- [ ] Add external student request handling
- [ ] Telegram bot integration
- [ ] Add reporting and analytics
- [ ] Export reports to Excel
- [ ] Build REST APIs
- [ ] Migrate the system to Django
- [ ] Add a web-based dashboard
- [ ] Explore AI / Generative AI features

---

# 🧠 What I Learned From This Project

This project represents a progression from beginner-level Python programming toward application architecture.

### Python

- Functions
- Classes
- Objects
- Methods
- Modules
- Exception handling
- File handling
- Context managers
- Type hints

### Database

- SQLite
- Table design
- Primary keys
- Foreign keys
- CRUD
- SQL queries
- Joins
- Transactions
- Database relationships

### Software Design

- Modular programming
- Separation of responsibilities
- Authentication
- Authorization
- Session management
- Role-based access control
- Audit trails

### Practical Development

- Debugging
- Refactoring
- Versioning
- Git/GitHub
- Feature-based development
- Incremental architecture

---

# 📌 Current Status

> 🟠 **Version 3.0.0 Beta — Active Development**

This release is functional but still under development. Some areas are intentionally being prepared for the next architectural stage.

The project should be viewed as a **learning-driven software project**, where each version represents a new stage of understanding and implementation.

---

# 👨‍💻 Author

### Subham Thakur

**Python Full Stack Development Learner**

Interested in:

`Python` · `Django` · `SQL` · `Web Development` · `AI` · `Generative AI`

---

## ⭐ If You Find This Project Interesting

This repository represents the complete learning journey from a simple Python CRUD application toward a more structured management system.

**Star ⭐ the repository and follow the development journey.**

---

> 💡 **Built step by step. Improved version by version.**
>
> **The code is the project — the version history is the story.**
