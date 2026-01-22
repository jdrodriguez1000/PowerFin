import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Add project root to sys.path
sys.path.append(os.getcwd())

import flet as ft
from views.pages.login_view import LoginView
from core.state import AppState

class TestPhase5SmartResend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ensure we don't actually hit the network
        from core.i18n import I18n
        I18n.load_language("es")

    def setUp(self):
        self.mock_page = MagicMock(spec=ft.Page)
        self.mock_page.url = "http://localhost:8551/#/login" # Mock URL for sanitization test
        self.mock_router = MagicMock()
        self.view = LoginView(self.mock_page, self.mock_router)
        
        # Mock AuthService part of the view instance directly or patch the class
        self.view.auth_service = MagicMock()
        
        # IMPORTANT: Call render to initialize form_container and validation widgets
        self.view.render()

    def test_smart_resend_trigger(self):
        """
        Test that receiving 'Email not confirmed' during login triggers the Smart Resend logic.
        """
        # Setup
        email = "unverified@test.com"
        password = "password123"
        
        # Simulate Sign In returning the specific error
        self.view.auth_service.sign_in.return_value = {
            "success": False, 
            "error": "Email not confirmed"
        }
        
        # Simulate Resend Success
        self.view.auth_service.resend_verification_email.return_value = {
            "success": True
        }
        
        # Set input values on the real Flet controls created in view.__init__
        # email_field is a Column, controls[1] is the TextField
        self.view.email_field.controls[1].value = email
        self.view.password_field.controls[1].value = password
        
        # Mock UI update methods to avoid Flet page update errors
        self.view._set_loading = MagicMock()
        self.view._show_error = MagicMock()
        self.view.show_verification_sent_view = MagicMock()
        self.view.restore_login_form = MagicMock() # Ensure this doesn't crash
        
        # Execute
        # We call handle_login(None) to simulate button click
        self.view.handle_login(None)
        
        # Verify
        # 1. Sign in was called
        self.view.auth_service.sign_in.assert_called_with(email, password)
        
        # 2. Resend verification was called (Logic inside handle_unconfirmed_login)
        # We need to verify that resend_verification_email was called with the email
        # and a redirect_url that comes from _sanitize_redirect_url
        
        # Expected sanitized URL from "http://localhost:8551/#/login" is "http://localhost:8551/"
        expected_redirect = "http://localhost:8551/"
        
        self.view.auth_service.resend_verification_email.assert_called_with(
            email, 
            redirect_to=expected_redirect
        )
        
        # 3. Success view was shown
        self.view.show_verification_sent_view.assert_called_with(email)

    def test_sanitize_redirect_url(self):
        """
        Test the URL sanitization logic specific to Phase 5 requirement.
        """
        # Case 1: Standard URL
        self.mock_page.url = "http://localhost:8551/#/login"
        sanitized = self.view._sanitize_redirect_url()
        self.assertEqual(sanitized, "http://localhost:8551/")
        
        # Case 2: URL with query params
        self.mock_page.url = "http://localhost:8551/?code=123#/onboarding"
        sanitized = self.view._sanitize_redirect_url()
        self.assertEqual(sanitized, "http://localhost:8551/")
        
        # Case 3: WebSocket replacement (unlikely in page.url but good to test logic)
        self.mock_page.url = "ws://localhost:8551/#/login"
        sanitized = self.view._sanitize_redirect_url()
        self.assertEqual(sanitized, "http://localhost:8551/")

if __name__ == "__main__":
    unittest.main()
