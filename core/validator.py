import re

class Validator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Checks if the email has a valid format."""
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return bool(re.match(pattern, email))

    @staticmethod
    def is_strong_password(password: str) -> bool:
        """
        Checks if the password meets security requirements:
        - Minimum 8 characters.
        """
        return len(password) >= 8

    @staticmethod
    def is_valid_name(name: str) -> bool:
        """Checks if the name is valid (at least 3 characters)."""
        return len(name.strip()) >= 3
