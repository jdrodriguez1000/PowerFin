import sys
import os
import unittest
from unittest.mock import MagicMock

# Add project root to sys.path
sys.path.append(os.getcwd())

import flet as ft
from core.i18n import I18n
from configs.routes import ROUTE_MAP
from views.pages.login_view import LoginView

class TestPhase3Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load languages for testing
        I18n.load_language("es")

    def test_routing_phase_3(self):
        """Verify that the root route and /login point to LoginView path."""
        print("Testing Route Configurations...")
        self.assertIn("/", ROUTE_MAP)
        self.assertIn("/login", ROUTE_MAP)
        
        # Check string paths
        self.assertEqual(ROUTE_MAP["/"], "views.pages.login_view.LoginView")
        self.assertEqual(ROUTE_MAP["/login"], "views.pages.login_view.LoginView")
        print("✅ Route config verified.")

    def test_i18n_login_keys(self):
        """Verify that mandatory keys for the new Login UI exist in Spanish."""
        print("Testing I18n Login Keys...")
        keys_to_test = [
            "auth.login.title",
            "auth.login.hero_title",
            "auth.login.hero_subtitle",
            "auth.login.email_label",
            "auth.login.password_label",
            "auth.login.submit"
        ]
        for key in keys_to_test:
            value = I18n.t(key)
            self.assertNotEqual(value, f"[{key}]", f"Missing translation for {key}")
            print(f"✅ Key {key}: {value}")

    def test_login_view_structure(self):
        """Verify the LoginView structure can be rendered without errors."""
        print("Testing LoginView rendering logic...")
        mock_page = MagicMock(spec=ft.Page)
        mock_router = MagicMock()
        
        # Initialize View
        view = LoginView(mock_page, mock_router)
        
        # Attempt to render
        try:
            content = view.render()
            self.assertIsInstance(content, ft.Row)
            # Check if it has 2 main sections (Hero and Form)
            self.assertEqual(len(content.controls), 2)
            print("✅ LoginView rendered successfully as ft.Row with 2 controls.")
        except Exception as e:
            self.fail(f"LoginView.render() failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
