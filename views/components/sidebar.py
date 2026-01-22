import flet as ft
from core.i18n import I18n
from core.theme import UserTheme

class Sidebar(ft.Container):
    def __init__(self, router, current_route="/", on_logout=None, user_name="User"):
        super().__init__()
        self.router = router
        self.current_route = current_route
        self.on_logout = on_logout
        self.user_name = user_name
        
        self.padding = ft.padding.symmetric(vertical=30, horizontal=20)
        self.width = 280
        # New dark green background
        self.bgcolor = "#032313" 
        self.border = ft.border.only(right=ft.BorderSide(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE10)))
        
        self.content = self._build_content()

    def _build_content(self):
        return ft.Column([
            # Brand Header & User Info - CENTERED
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.AUTO_AWESOME_ROUNDED, color="#B6F09C", size=28),
                        ft.Text("PowerFin", size=24, weight=ft.FontWeight.W_900, color=ft.Colors.WHITE),
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                    ft.Column([
                        ft.Text(self.user_name, size=14, weight=ft.FontWeight.W_700, color=ft.Colors.WHITE),
                        ft.Text("22 de Enero, 2026", size=12, color=ft.Colors.WHITE70),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
                padding=ft.padding.only(bottom=10)
            ),
            
            # 3. Separator after name/date
            ft.Divider(height=20, color=ft.Colors.WHITE10),
            
            # Primary Navigation
            self._build_item(ft.Icons.DASHBOARD_ROUNDED, "dashboard.menu.dashboard", "/"),
            
            # 4. Separator after Resumen
            ft.Divider(height=20, color=ft.Colors.WHITE10),
            
            self._build_item(ft.Icons.PIE_CHART_ROUNDED, "dashboard.menu.budget", "/construction"),
            self._build_item(ft.Icons.TRACK_CHANGES_ROUNDED, "dashboard.menu.goals", "/construction"),
            self._build_item(ft.Icons.SWAP_HORIZ_ROUNDED, "dashboard.menu.transactions", "/construction"),
            self._build_item(ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, "dashboard.menu.accounts", "/construction"),
            
            # 2. Separator after Cuentas
            ft.Divider(height=20, color=ft.Colors.WHITE10),
            
            ft.Container(height=10), # Vertical space
            
            # Secondary Navigation
            self._build_item(ft.Icons.PERSON_OUTLINE_ROUNDED, "dashboard.menu.profile", "/construction"),
            self._build_item(ft.Icons.SETTINGS_OUTLINED, "dashboard.menu.settings", "/construction"),
            
            ft.Container(expand=True),
            
            # Logout
            self._build_item(ft.Icons.LOGOUT_ROUNDED, "dashboard.menu.logout", on_click=self.on_logout),
        ], spacing=5)

    def _build_item(self, icon, label_key, route=None, on_click=None):
        active = self.current_route == route if route else False
        
        # Colors for DARK background
        active_bg = "#B6F09C"      # High contrast lime for active
        active_text = "#032313"    # Dark green text on lime bg
        inactive_text = ft.Colors.WHITE70
        
        def handle_click(e):
            if on_click:
                on_click(e)
            elif route:
                self.router.navigate(route)

        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=active_text if active else inactive_text, size=20),
                ft.Text(
                    I18n.t(label_key), 
                    color=active_text if active else inactive_text, 
                    weight=ft.FontWeight.W_700 if active else ft.FontWeight.W_500, 
                    size=14
                ),
            ], spacing=12),
            padding=ft.padding.symmetric(vertical=10, horizontal=15),
            border_radius=12,
            bgcolor=active_bg if active else None,
            on_click=handle_click,
            ink=True,
            on_hover=lambda e: None if active else setattr(e.control, "bgcolor", ft.Colors.WHITE10) if e.data == "true" else setattr(e.control, "bgcolor", None)
        )
