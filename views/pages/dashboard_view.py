import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.auth_service import AuthService
from core.profile_service import ProfileService
from core.logger import Logger
from views.components.sidebar import Sidebar
from views.components.summary_card import SummaryCard
from views.components.quick_action import QuickAction

from core.state import AppState

class DashboardView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        self.auth_service = AuthService()
        self.profile_service = ProfileService()
        
        # User state
        self.user = None
        self.profile = None
        self.full_name = "User"
        
        # UI controls
        self.balance_text = ft.Text("$ 0.00", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.autonomy_text = ft.Text("0", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.savings_text = ft.Text("$ 0.00", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.passive_index_text = ft.Text("0 %", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    def handle_logout(self, _):
        self.auth_service.sign_out()
        AppState.user = None
        self.router.navigate("/login")

    def render(self):
        # 1. Fetch Data
        user_res = self.auth_service.get_current_user()
        if user_res and user_res.user:
            self.user = user_res.user
            profile_res = self.profile_service.get_profile(self.user.id)
            if profile_res["success"]:
                self.profile = profile_res["profile"]
                self.full_name = self.profile.full_name
                # Placeholder for balance; in next phases we'll fetch actual accounts
                currency = self.profile.currency_code if self.profile.currency_code else "$"
                self.balance_text.value = f"{currency} 0.00"
                self.savings_text.value = f"{currency} 0.00"
                self.passive_index_text.value = "0 %"
        else:
            # This should ideally not happen due to route guarding
            Logger.warning("DashboardView rendered without an authenticated user.")
            self.router.navigate("/login")
            return ft.Container() # Return empty while redirecting
        
        # 2. Build Sidebar
        sidebar = Sidebar(self.router, current_route="/", on_logout=self.handle_logout, user_name=self.full_name)

        # 3. Build Header
        header = ft.Row([
            ft.Column([
                ft.Text(I18n.t("dashboard.menu.dashboard"), 
                        size=34, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY),
            ], spacing=4),
            ft.Row([
                ft.IconButton(ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.GREY_700),
                ft.Container(
                    content=ft.CircleAvatar(
                        content=ft.Text(
                            self.full_name[0].upper() if self.full_name else "U",
                            color=UserTheme.SECONDARY
                        ),
                        bgcolor=UserTheme.PRIMARY,
                    ),
                    padding=2
                )
            ], spacing=10)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # 4. Build Summary Cards per PRD Order
        cards_row = ft.Row([
            SummaryCard("dashboard.balance", self.balance_text, ft.Icons.ACCOUNT_BALANCE_WALLET_ROUNDED, UserTheme.SECONDARY),
            SummaryCard("dashboard.savings", self.savings_text, ft.Icons.SAVINGS_ROUNDED, "#4F46E5"),
            SummaryCard("dashboard.autonomy", self.autonomy_text, ft.Icons.TIMER_OUTLINED, "#0891B2"),
            SummaryCard("dashboard.passive_index", self.passive_index_text, ft.Icons.PERCENT_ROUNDED, "#EA580C"),
        ], spacing=20, scroll=ft.ScrollMode.ADAPTIVE)

        # 5. Quick Actions
        quick_actions = ft.Container(
            content=ft.Column([
                ft.Text(I18n.t("dashboard.quick_actions"), size=18, weight=ft.FontWeight.W_700, color=UserTheme.SECONDARY),
                ft.Row([
                    QuickAction(ft.Icons.ADD_CIRCLE_OUTLINE, "dashboard.add_income", ft.Colors.GREEN_600),
                    QuickAction(ft.Icons.REMOVE_CIRCLE_OUTLINE, "dashboard.add_expense", ft.Colors.RED_600),
                    QuickAction(ft.Icons.SWAP_HORIZ_ROUNDED, "dashboard.menu.transactions", ft.Colors.BLUE_600),
                    QuickAction(ft.Icons.MORE_HORIZ_ROUNDED, "common.buttons.next", ft.Colors.GREY_600),
                ], spacing=10, run_spacing=10, wrap=True, alignment=ft.MainAxisAlignment.START),
            ], spacing=20),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK), offset=ft.Offset(0, 5))
        )

        # 6. Health Section (Salud Patrimonial)
        health_section = ft.Container(
            content=ft.Column([
                ft.Text(I18n.t("dashboard.health.title").upper(), size=13, weight=ft.FontWeight.W_700, color=ft.Colors.GREY_500),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                             ft.Icon(ft.Icons.PIE_CHART_ROUNDED, color=ft.Colors.BLUE_GREY_400, size=20),
                             ft.Text(I18n.t("dashboard.health.iec"), size=13, weight=ft.FontWeight.W_500, color=ft.Colors.BLUE_GREY_400),
                            ft.Text("0.0 %", size=24, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY),
                        ], spacing=8),
                        padding=25, 
                        bgcolor=ft.Colors.WHITE, 
                        border_radius=20, 
                        expand=True,
                        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.03, ft.Colors.BLACK))
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.Icons.MONETIZATION_ON_OUTLINED, color=ft.Colors.RED_300, size=20),
                            ft.Text(I18n.t("dashboard.health.opportunity_cost"), size=13, weight=ft.FontWeight.W_500, color=ft.Colors.BLUE_GREY_400),
                            ft.Text("$ 0.00", size=24, weight=ft.FontWeight.W_800, color=ft.Colors.RED_400),
                        ], spacing=8),
                        padding=25, 
                        bgcolor=ft.Colors.WHITE, 
                        border_radius=20, 
                        expand=True,
                        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.03, ft.Colors.BLACK))
                    ),
                ], spacing=25)
            ], spacing=20),
            padding=ft.padding.only(top=10)
        )

        # 7. Main Content Layout
        main_content = ft.Container(
            content=ft.Column([
                header,
                ft.Container(height=40),
                cards_row,
                ft.Container(height=40),
                health_section,
                ft.Container(height=40),
                quick_actions,
            ], spacing=0, scroll=ft.ScrollMode.ADAPTIVE),
            padding=40,
            expand=True,
            bgcolor=UserTheme.BACKGROUND, 
        )

        return ft.Row([
            sidebar,
            main_content,
        ], expand=True, spacing=0)
