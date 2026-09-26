class UserSession:

    current_user = None
    current_role = None

    @classmethod
    def login(cls, user_id, role):
        cls.current_user = user_id
        cls.current_role = role

    @classmethod
    def logout(cls):
        cls.current_user = None
        cls.current_role = None

    @classmethod
    def get_user(cls):
        return cls.current_user

    @classmethod
    def get_role(cls):
        return cls.current_role