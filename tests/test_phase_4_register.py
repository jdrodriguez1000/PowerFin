import sys
import os
import unittest
from unittest.mock import MagicMock

# Add project root to sys.path
sys.path.append(os.getcwd())

import flet as ft
from core.i18n import I18n
from configs.routes import ROUTE_MAP
from views.pages.register_view import RegisterView

class TestPhase4Register(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        I18n.load_language("es")

    def test_routing_phase_4(self):
        """Verify that the /register route exists and points to the right path."""
        self.assertIn("/register", ROUTE_MAP)
        self.assertEqual(ROUTE_MAP["/register"], "views.pages.register_view.RegisterView")

    def test_i18n_register_keys(self):
        """Verify that mandatory keys for the Register UI exist."""
        keys_to_test = [
            "auth.register.title",
            "auth.register.name_label",
            "auth.register.email_label",
            "auth.register.password_label",
            "auth.register.submit",
            "auth.register.hero_title"
        ]
        for key in keys_to_test:
            value = I18n.t(key)
            self.assertNotEqual(value, f"[{key}]", f"Missing translation for {key}")

    def test_register_view_render(self):
        """Verify RegisterView can be instantiated and rendered."""
        mock_page = MagicMock(spec=ft.Page)
        mock_router = MagicMock()
        
        view = RegisterView(mock_page, mock_router)
        content = view.render()
        
        self.assertIsInstance(content, ft.Row)
        self.assertEqual(len(content.controls), 2) # Hero and Form

if __name__ == "__main__":
    unittest.main()
