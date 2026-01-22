import flet as ft
from core.i18n import I18n
from core.theme import UserTheme

class Sidebar(ft.Container):
    def __init__(self, router, current_route="/", on_logout=None):
        super().__init__()
        self.router = router
        self.current_route = current_route
        self.on_logout = on_logout
        
        self.padding = 30
        self.width = 280
        self.bgcolor = ft.Colors.WHITE
        self.border = ft.border.only(right=ft.BorderSide(1, UserTheme.DIVIDER))
        
        self.content = self._build_content()

    def _build_content(self):
        return ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.AUTO_AWESOME_ROUNDED, color=UserTheme.PRIMARY, size=30),
                    ft.Text("PowerFin", size=22, weight=ft.FontWeight.W_900, color=UserTheme.SECONDARY),
                ], spacing=10),
                padding=ft.padding.only(bottom=40, left=10)
            ),
            self._build_item(ft.Icons.DASHBOARD_ROUNDED, "dashboard.menu.dashboard", "/"),
            self._build_item(ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, "dashboard.menu.accounts", "/construction"),
            self._build_item(ft.Icons.SWAP_HORIZ_ROUNDED, "dashboard.menu.transactions", "/construction"),
            self._build_item(ft.Icons.TRACK_CHANGES_ROUNDED, "dashboard.menu.goals", "/construction"),
            ft.Divider(height=40, color=UserTheme.DIVIDER),
            self._build_item(ft.Icons.PERSON_OUTLINE_ROUNDED, "dashboard.menu.profile", "/construction"),
            self._build_item(ft.Icons.SETTINGS_OUTLINED, "dashboard.menu.settings", "/construction"),
            ft.Container(expand=True),
            self._build_item(ft.Icons.LOGOUT_ROUNDED, "dashboard.menu.logout", on_click=self.on_logout),
        ], spacing=5)

    def _build_item(self, icon, label_key, route=None, on_click=None):
        active = self.current_route == route if route else False
        color = UserTheme.PRIMARY if active else UserTheme.TEXT_DISABLED
        
        def handle_click(e):
            if on_click:
                on_click(e)
            elif route:
                self.router.navigate(route)

        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=color, size=24),
                ft.Text(I18n.t(label_key), color=color, weight=ft.FontWeight.W_600 if active else ft.FontWeight.NORMAL, size=15),
            ], spacing=15),
            padding=ft.padding.symmetric(vertical=12, horizontal=20),
            border_radius=10,
            on_click=handle_click,
            ink=True,
            bgcolor=ft.Colors.with_opacity(0.1, UserTheme.PRIMARY) if active else None,
        )
