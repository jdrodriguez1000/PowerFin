import flet as ft
from core.i18n import I18n
from core.theme import UserTheme

class LoginView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        self.page.bgcolor = ft.Colors.WHITE
        self.page.padding = 0

    def render(self):
        LINK_BLUE = "#0D47A1"
        
        # --- LEFT SIDE: THE HERO IMAGE ---
        hero_side = ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLACK,
            content=ft.Stack([
                # Background Image
                ft.Image(
                    src="/imgs/login_bg.png",
                    fit=ft.BoxFit.COVER,
                    expand=True,
                ),
                # Gradient & Dark Overlay
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.BOTTOM_CENTER,
                        end=ft.Alignment.TOP_CENTER,
                        colors=["#D5000000", "#44000000"]
                    ),
                    expand=True,
                ),
                # Content Layer
                ft.Container(
                    content=ft.Column([
                        # Top Part
                        ft.Row([
                            ft.Container(
                                content=ft.Icon(ft.Icons.MONETIZATION_ON_ROUNDED, color=UserTheme.PRIMARY, size=32),
                                bgcolor=ft.Colors.WHITE,
                                padding=8,
                                border_radius=50,
                            ),
                            ft.Text("PowerFin", size=26, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                        ], spacing=15),
                        
                        # Bottom Part
                        ft.Column([
                            ft.Text(
                                I18n.t("auth.login.hero_title"), 
                                size=44, 
                                weight=ft.FontWeight.BOLD, 
                                color=ft.Colors.WHITE,
                                width=400,
                            ),
                            ft.Text(
                                I18n.t("auth.login.hero_subtitle"), 
                                size=18, 
                                color=ft.Colors.WHITE,
                                opacity=0.8,
                            ),
                        ], spacing=10),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=60,
                    margin=ft.margin.only(bottom=40),
                    expand=True,
                )
            ], expand=True),
        )

        # --- RIGHT SIDE: THE LOGIN FORM ---
        def on_hover(e):
            e.control.scale = 1.02 if e.data == "true" else 1.0
            e.control.update()

        login_form = ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            alignment=ft.Alignment.CENTER, # Center the Column within the panel
            content=ft.Container(
                width=420,
                content=ft.Column([
                    # Header
                    ft.Column([
                        ft.Text(I18n.t("auth.login.title"), size=38, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY),
                        ft.Text(I18n.t("auth.login.subtitle"), size=15, color=ft.Colors.GREY_600),
                    ], spacing=2),
                    
                    ft.Container(height=40),
                    
                    # Inputs
                    ft.Column([
                        ft.Text(I18n.t("auth.login.email_label"), weight=ft.FontWeight.BOLD, size=12, color=UserTheme.SECONDARY),
                        ft.TextField(
                            hint_text=I18n.t("auth.login.email_hint"),
                            border_radius=8,
                            border_color=ft.Colors.GREY_300,
                            focused_border_color=UserTheme.PRIMARY,
                            bgcolor="#FDFDFD",
                            color=ft.Colors.BLACK,
                            height=52,
                            width=float("inf"),
                            text_size=16,
                            content_padding=ft.padding.symmetric(horizontal=15),
                        ),
                    ], spacing=6),

                    ft.Container(height=12),

                    ft.Column([
                        ft.Text(I18n.t("auth.login.password_label"), weight=ft.FontWeight.BOLD, size=12, color=UserTheme.SECONDARY),
                        ft.TextField(
                            hint_text=I18n.t("auth.login.password_hint"),
                            border_radius=8,
                            border_color=ft.Colors.GREY_300,
                            focused_border_color=UserTheme.PRIMARY,
                            bgcolor="#FDFDFD",
                            color=ft.Colors.BLACK,
                            height=52,
                            width=float("inf"),
                            text_size=16,
                            password=True,
                            can_reveal_password=True,
                            content_padding=ft.padding.symmetric(horizontal=15),
                        ),
                    ], spacing=6),

                    ft.Container(height=10),

                    # Remember/Forgot
                    ft.Row([
                        ft.Row([
                            ft.Checkbox(fill_color=UserTheme.PRIMARY, scale=0.9),
                            ft.Text(I18n.t("auth.login.remember_me"), color=ft.Colors.BLACK, size=13, weight=ft.FontWeight.W_600),
                        ], spacing=0),
                        ft.TextButton(
                            content=ft.Text(I18n.t("auth.login.forgot_password"), color=LINK_BLUE, size=12),
                            on_click=lambda _: self.router.navigate("/construction")
                        ),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                    ft.Container(height=35),

                    # Login button
                    ft.ElevatedButton(
                        content=ft.Text(I18n.t("auth.login.submit"), size=16, weight=ft.FontWeight.BOLD, color=UserTheme.SECONDARY),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            bgcolor={
                                ft.ControlState.HOVERED: UserTheme.PRIMARY,
                                ft.ControlState.DEFAULT: UserTheme.PRIMARY,
                            },
                        ),
                        width=float("inf"),
                        height=55,
                        on_hover=on_hover,
                        on_click=lambda _: self.router.navigate("/construction")
                    ),

                    ft.Container(height=45),

                    # Footer
                    ft.Row([
                        ft.Text(I18n.t("auth.login.no_account"), color=ft.Colors.GREY_500, size=13),
                        ft.TextButton(
                            content=ft.Text(I18n.t("auth.login.register"), color=LINK_BLUE, weight=ft.FontWeight.BOLD, size=13),
                            on_click=lambda _: self.router.navigate("/construction")
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),

                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
            ),
        )

        return ft.Row([hero_side, login_form], expand=True, spacing=0)
