from core.database import Database
from core.logger import Logger
import flet as ft

class AuthService:
    def __init__(self):
        self.db = Database.get_client()

    def sign_up(self, email, password, full_name, redirect_to=None):
        """
        Registers a new user in Supabase Auth.
        The trigger in the database will handle profile creation.
        """
        try:
            Logger.info(f"Attempting signup for: {email}")
            options = {
                "data": {
                    "full_name": full_name
                }
            }
            if redirect_to:
                options["email_redirect_to"] = redirect_to

            # Positional dictionary for compatibility with current supabase-py version
            credentials = {
                "email": email,
                "password": password,
                "options": options
            }
            res = self.db.auth.sign_up(credentials)
            
            Logger.info(f"Signup successful for: {email}")
            return {"success": True, "user": res.user}
        except Exception as e:
            error_msg = str(e)
            Logger.error(f"Signup error: {error_msg}")
            return {"success": False, "error": error_msg}

    def sign_in(self, email, password):
        """
        Authenticates a user.
        """
        try:
            Logger.info(f"Attempting login for: {email}")
            credentials = {
                "email": email,
                "password": password
            }
            res = self.db.auth.sign_in_with_password(credentials)
            Logger.info(f"Login successful for: {email}")
            return {"success": True, "user": res.user, "session": res.session}
        except Exception as e:
            error_msg = str(e)
            Logger.error(f"Login error: {error_msg}")
            return {"success": False, "error": error_msg}

    def sign_out(self):
        """
        Logs out the current user.
        """
        try:
            self.db.auth.sign_out()
            Logger.info("User signed out.")
            return True
        except Exception as e:
            Logger.error(f"Signout error: {str(e)}")
            return False

    def get_current_user(self):
        """
        Returns the current authenticated user if exists.
        """
        return self.db.auth.get_user()

    def resend_verification_email(self, email, redirect_to=None):
        """
        Resends the signup confirmation email to the user.
        """
        try:
            Logger.info(f"Resending verification email to: {email}")
            options = {
                "type": "signup",
                "email": email
            }
            if redirect_to:
                options["options"] = {"email_redirect_to": redirect_to}
                
            self.db.auth.resend(options)
            Logger.info(f"Verification email resent to: {email}")
            return {"success": True}
        except Exception as e:
            error_msg = str(e)
            Logger.error(f"Resend verification error: {error_msg}")
            return {"success": False, "error": error_msg}
