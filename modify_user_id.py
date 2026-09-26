from db_config import Database
import sqlite3
def modify_user_id():
    db = Database()
    con: sqlite3.Connection = db.create_connection()
    cursor: sqlite3.Cursor = con.cursor()
    user_id: str = input("Enter your user id you want to change: ")
    cursor.execute("""
                    SELECT user_id, password
                    FROM user_auth
                    WHERE user_id =?
                    """,(user_id,))
    fetch = cursor.fetchone()
    if not fetch:
        con.close()
        print("No user id found!")
        return
    id = fetch[0]
    password = fetch[1]
    print("Details Found!")
    verify_password: str = input("Enter password: ")
    if verify_password != password:
        print("Password Not match")
        return
    print("Password match!")
    new_id: str = input("Enter new user id: ")
    if new_id == id:
        print("User id not available")
        return
    try:
        cursor.execute("""
                        UPDATE user_auth
                        SET user_id =?
                        WHERE password =?
                        """,(new_id, password))
        con.commit()
        print(f"User id update done new user id {new_id}")
    except sqlite3.IntegrityError as e:
        print(f"User id Already exists")
    finally:
        con.close()

