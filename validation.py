import re
from string import digits


class Validation:

    # ---------------- NAME VALIDATION ----------------

    @staticmethod
    def validate_name(name):

        pattern = r"^[A-Za-z ]+$"

        if re.fullmatch(pattern, name):
            return True

        return False

    # ---------------- DOB VALIDATION ----------------

    @staticmethod
    def validate_dob(dob):

        pattern = r"^\d{2}/\d{2}/\d{4}$"

        if re.fullmatch(pattern, dob):
            return True

        return False

    # ---------------- QUALIFICATION VALIDATION ----------------

    @staticmethod
    def validate_qualification(education):

        pattern = r"^[A-Za-z .]+$"

        if re.fullmatch(pattern, education):
            return True

        return False

    # ---------------- COURSE VALIDATION ----------------

    @staticmethod
    def validate_course(course):

        pattern = r"^[A-Za-z ]+$"

        if re.fullmatch(pattern, course):
            return True

        return False

    # ---------------- ADMISSION STATUS VALIDATION ----------------

    @staticmethod
    def validate_status(admission):

        pattern = r"^(Pending|Approved|Rejected)$"

        if re.fullmatch(pattern, admission, re.IGNORECASE):
            return True

        return False

    # ---------------- OPTION VALIDATION ----------------

    # @staticmethod
    # def validate_option(option):

    #     pattern = r"^[1-9]$"

    #     if re.fullmatch(pattern, option):
    #         return True

    #     return False

    # ---------------- YES / NO VALIDATION ----------------

    # @staticmethod
    # def validate_yes_no(value):

    #     pattern = r"^(Yes|No)$"

    #     if re.fullmatch(pattern, value, re.IGNORECASE):
    #         return True

    #     return False
    
    # ---------------- ADDRESS VALIDATION ----------------
    @staticmethod
    def validate_address(adress): 
        pattern = r"^[A-Za-z0-9\s,./#-]+$" 
        if re.fullmatch(pattern, adress): 
            return True 
        return False
    
    # ---------------- COURSE DURATION VALIDATION ----------------
    @staticmethod 
    def validate_course_duration(course_duration): 
        pattern = r"^[1-9] (month|months)$" 
        if re.fullmatch(pattern, course_duration): 
            return True 
        return False

    # ---------------- USER_ID VALIDATION ----------------
    @staticmethod
    def validate_user_id(user_id):

        # Must contain at least 4 alphabets
        alphabets = re.findall(r"[A-Za-z]", user_id)

        # Must contain at least 2 digits
        digits = re.findall(r"[0-9]", user_id)

        # Only alphabets and digits are allowed
        if not re.fullmatch(r"[A-Za-z0-9]+", user_id):
            return False

        if len(alphabets) < 4:
            return False

        if len(digits) < 2:
            return False

        return True

    # ---------------- PASSWORD VALIDATION ----------------
    @staticmethod
    def validate_password(password):

        # Must contain at least 4 alphabets
        alphabets = re.findall(r"[A-Za-z]", password)

        # Must contain at least 4 digits
        digits = re.findall(r"[0-9]", password)

        # Special characters except ! ; : ' &
        special_characters = re.findall(r"[^A-Za-z0-9!;:'&]", password)

        if len(alphabets) < 4:
            return False

        if len(digits) < 4:
            return False

        if len(special_characters) < 2:
            return False

        # Make sure forbidden characters are not present
        if re.search(r"[!;:'&]", password):
            return False

        return True
    
    # ---------------- COURSE TOPIC VALIDATION ----------------
    @staticmethod
    def validate_course_topic(course_topic):
        pattern = r"^[A-Za-z, ]+$"

        if re.fullmatch(pattern, course_topic):
            return True

        return False
