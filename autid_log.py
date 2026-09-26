import sqlite3
from user_session import UserSession


def add_audit_log(action, description):

    user_id = UserSession.get_user()

    connection = sqlite3.connect("student_DB.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO audit_log
        (user_id, action, description)
        VALUES (?, ?, ?)
    """, (user_id, action, description))

    connection.commit()
    connection.close()


def view_audit_logs():

    connection = sqlite3.connect("student_DB.db")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            log_id,
            user_id,
            action,
            description,
            log_time
        FROM audit_log
        ORDER BY log_id DESC
    """)

    logs = cursor.fetchall()

    print("\n========== AUDIT LOG ==========")

    if not logs:
        print("No audit logs found.")

    else:
        for log in logs:
            print(f"""
Log ID     : {log['log_id']}
User ID    : {log['user_id']}
Action     : {log['action']}
Description: {log['description']}
Time       : {log['log_time']}
-------------------------------
""")

    connection.close()
    
