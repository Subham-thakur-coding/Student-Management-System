from user_session import UserSession



# ROLE PERMISSIONS


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



# CHECK PERMISSION


def has_permission(permission):

    role = UserSession.get_role()
    if role is None:
        return False
    return permission in PERMISSIONS.get(role, set())



# REQUIRE PERMISSION


def require_permission(permission):

    if has_permission(permission):
        return True

    print("\n========================================")
    print("             ACCESS DENIED")
    print("========================================")
    print("You do not have permission to access")
    print(f"the '{permission}' section.")
    print("========================================")

    return False