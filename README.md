# 🎓 Student Management System — v3.0.1 Beta

A **Python + SQLite console-based Student Management System** that manages student records through role-based access, department queues, admission processing, payment tracking, and faculty activation.

> **🚧 Project status: Beta / Under development**
>
> `v3.0.1-beta` is a development release. Features and workflows may change, and this version should be tested before being used with real student data.

---

## ✨ What's New in v3.0.1 Beta?

This version expands the earlier student and course management project into a department-based workflow.

- 🔐 **Role-based access control (RBAC):** menus and operations are restricted according to the logged-in user's role.
- 👥 **User sessions:** the application keeps track of the current user's ID and role during the session.
- 🔑 **Password utilities:** password hashing and password-checking functions are included.
- 🧾 **Audit logging:** records selected user actions for tracking and review.
- 📥 **Database-backed queues:** students are placed in department queues and processed in FIFO order.
- 🏫 **Admission processing:** admission staff add course details such as course name, duration, topic, and faculty member.
- 💳 **Payment processing:** payment staff record amount, payment method, date/time, and status.
- 🔁 **Return workflow:** rejected payments can be sent back for administrative follow-up; pending payments remain in the payment workflow.
- 🎓 **Faculty workflow:** faculty can review students in the faculty queue and activate eligible students.
- 📋 **Active student records:** activation copies student and course information into the `active_students` table.
- 📲 **Telegram notification module:** includes code to send a notification using active-student information.
- 🧰 **Input validation:** validation functions help check user input.
- 💬 **Exit feedback:** feedback can be saved to a CSV file.
- 🔄 **Password recovery and migration utilities:** supporting modules are included in the project.

---

## 🔄 Student Workflow

```text
ADMIN
  │ Add student details
  ▼
ADMISSION QUEUE
  │ Add course details
  ▼
PAYMENT QUEUE
  │ Record payment details
  ├── Pending ──► Remains in payment workflow
  ├── Rejected ─► Returned for administrative follow-up
  └── Approved
          │
          ▼
    FACULTY QUEUE
          │ Review and activate
          ▼
    ACTIVE STUDENT
```

The queue manager stores queue entries in SQLite and selects waiting students in ascending queue-ID order, which supports **first-in, first-out (FIFO)** processing.

---

## 🔐 Roles and Access

The project defines role permissions in `authorization.py`.

| Role | Main access |
|---|---|
| `devops` | Student, course, admission, payment, account, user/role management, audit, faculty, and queue features |
| `admin` | Student, course, admission, payment, account, role changes, audit, faculty, and queue features |
| `admission` | Admission operations, account, and password change |
| `payment` | Payment operations, account, and password change |
| `faculty` | Faculty workflow |

Actual access depends on the permission checks used by each menu.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Application logic |
| **SQLite** | Local relational database |
| **SQL** | Database queries and updates |
| **OOP and modules** | Organizing application code |
| **Regular expressions / validation functions** | Input validation |
| **CSV** | Feedback and file-based data handling |
| **`hashlib`** | Password hashing utility |
| **Telegram Bot API** | Optional notifications |
| **`requests`** | HTTP requests for Telegram notifications |

---

## 📁 Project Structure

```text
student_database_sqlite_v.3.0.01beta/
├── main.py
├── main_menu.py
├── db_config.py
├── validation.py
├── authorization.py
├── user_session.py
├── password_util.py
├── migration.py
├── forgot_password.py
├── add_admin.py
├── modify_user.py
├── remove_admin.py
├── add_student.py
├── delete_student.py
├── admission_menu.py
├── process_admission.py
├── return_admission.py
├── payment_menu.py
├── process_payment.py
├── return_student.py
├── faculty_menu.py
├── activate_student.py
├── view_active_student.py
├── queue_manager.py
├── view_queue.py
├── autid_log.py
├── feedback.py
├── feedback.csv
├── telegram_notification.py
└── student_DB.db
```

The SQLite database file may be created or updated when the application runs. Keep database files containing personal information private.

---

## ▶️ Getting Started

### 1. Install Python

Install a supported Python 3 version and confirm that Python is available in your terminal:

```bash
python --version
```

### 2. Download or clone the repository

Replace the placeholder with your own GitHub repository URL:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 3. Install the notification dependency

If you want to use Telegram notifications, install `requests`:

```bash
python -m pip install requests
```

The core console/database features use Python's built-in `sqlite3` module.

### 4. Run the application

```bash
python main.py
```

Follow the prompts in the terminal to log in and open the available menu for your role.

> **Important:** Check the authentication setup in `db_config.py` before first use. Do not rely on default credentials for a real deployment; change them and use unique, strong passwords.

---

## 🗃️ Main Database Areas

The application creates and uses tables for different parts of the workflow, including:

- **`user_auth`** — user IDs, password values, and roles.
- **`student_details`** — student personal and education details.
- **`course_details`** — course information associated with students.
- **`student_queue`** — department queue entries and queue status.
- **Payment records** — payment amount, method, date/time, and status.
- **`active_students`** — details copied when a student is activated.
- **Audit records** — selected actions performed in the application.

The exact schema depends on the database initialization and migration code in this version.

---

## 🛡️ Security Notes

This is a learning project and is **not yet production-ready**.

- Do not commit real student information or a populated database to a public repository.
- Do not store bot tokens, chat IDs, or other secrets directly in source code. Load them from environment variables.
- **Before publishing this version, rotate/revoke any Telegram bot token that has been committed or shared**, then update `telegram_notification.py` to read `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` from environment variables.
- The current `password_util.py` uses SHA-256 directly. For real applications, use a password-hashing algorithm designed for passwords, such as **Argon2id** or **PBKDF2** with a unique salt and appropriate parameters.
- Test password recovery, role permissions, queue transitions, and database migrations before relying on them.
- Back up the database before running migration or testing code that changes records.

---

## 🧠 Concepts Practiced

- Python functions, classes, modules, loops, and exception handling
- SQLite connections, table creation, and CRUD operations
- Authentication, sessions, and role-based permissions
- Password hashing concepts
- FIFO queue processing
- Multi-step student workflows
- Input validation
- Audit logging
- CSV file handling and context managers
- Integrating an external API

---

## 🗺️ Possible Next Improvements

- Use a password-hashing scheme designed for passwords, with salts and work factors.
- Move secrets to environment variables and add a `.env.example` file without real credentials.
- Add automated tests for permissions, payments, and queue transitions.
- Improve error handling and database transaction management.
- Add safer database backup and CSV export/import tools.
- Build a Django web interface after the console workflow is stable.

---

## 👨‍💻 Author

**Subham Thakur**  
Python Full Stack Development Learner

**Built with:** `Python` · `SQLite` · `SQL` · `RBAC` · `CSV` · `Telegram Bot API`

---

## 📌 Release Information

- **Version:** `v3.0.1-beta`
- **Status:** Beta / Under development
- **Suggested Git tag:** `v3.0.1-beta`

This release continues the project from basic student and course management toward a role-based, queue-driven student lifecycle system.

---

## 📜 License

No license file was identified in this project archive. Add a `LICENSE` file before presenting the repository as open source, and choose a license that matches how you want others to use the project.
