import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.validator import Validator
from views.components.auth_layout import AuthLayout

class LoginView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        self.page.bgcolor = ft.Colors.WHITE
        self.page.padding = 0
        
        # Form Controls
        self.email_field = self._build_textfield(
            label_key="auth.login.email_label",
            hint_key="auth.login.email_hint",
            icon=ft.Icons.EMAIL_OUTLINED
        )
        self.password_field = self._build_textfield(
            label_key="auth.login.password_label",
            hint_key="auth.login.password_hint",
            icon=ft.Icons.LOCK_OUTLINE,
            password=True
        )
        self.error_text = ft.Text("", color=ft.Colors.RED_400, size=12, weight=ft.FontWeight.W_500)
        
        # Loading state
        self.progress_ring = ft.ProgressRing(width=16, height=16, stroke_width=2, color=UserTheme.SECONDARY, visible=False)
        self.submit_button_text = ft.Text(I18n.t("auth.login.submit"), size=16, weight=ft.FontWeight.BOLD, color=UserTheme.SECONDARY)

    def _build_textfield(self, label_key, hint_key, icon, password=False):
        return ft.Column([
            ft.Text(I18n.t(label_key), weight=ft.FontWeight.BOLD, size=12, color=UserTheme.SECONDARY),
            ft.TextField(
                hint_text=I18n.t(hint_key),
                border_radius=8,
                border_color=ft.Colors.GREY_300,
                focused_border_color=UserTheme.PRIMARY,
                bgcolor="#FDFDFD",
                color=ft.Colors.BLACK,
                height=52,
                width=float("inf"),
                text_size=16,
                password=password,
                can_reveal_password=password,
                prefix_icon=icon,
                content_padding=ft.padding.symmetric(horizontal=15),
            ),
        ], spacing=6)

    def handle_login(self, e):
        email = self.email_field.controls[1].value.strip()
        password = self.password_field.controls[1].value
        
        if not Validator.is_valid_email(email):
            self.error_text.value = I18n.t("validation.email_invalid")
            self.page.update()
            return
            
        if not password:
            self.error_text.value = I18n.t("auth.login.password_hint") # Basic check
            self.page.update()
            return

        self.error_text.value = ""
        self.router.navigate("/construction")

    def render(self):
        LINK_BLUE = "#0D47A1"
        
        def on_hover(e):
            if not e.control.disabled:
                e.control.scale = 1.02 if e.data == "true" else 1.0
                e.control.update()

        login_form_content = ft.Column([
            # Header
            ft.Column([
                ft.Text(I18n.t("auth.login.title"), size=38, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY),
                ft.Text(I18n.t("auth.login.subtitle"), size=15, color=ft.Colors.GREY_600),
            ], spacing=2),
            
            ft.Container(height=40),
            
            self.email_field,
            ft.Container(height=12),
            self.password_field,
            
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

            self.error_text,
            ft.Container(height=25),

            # Login button
            ft.ElevatedButton(
                content=ft.Row([self.submit_button_text, self.progress_ring], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    bgcolor={ft.ControlState.HOVERED: UserTheme.PRIMARY, ft.ControlState.DEFAULT: UserTheme.PRIMARY},
                ),
                width=float("inf"),
                height=55,
                on_hover=on_hover,
                on_click=self.handle_login
            ),

            ft.Container(height=45),

            # Footer
            ft.Row([
                ft.Text(I18n.t("auth.login.no_account"), color=ft.Colors.GREY_500, size=13),
                ft.TextButton(
                    content=ft.Text(I18n.t("auth.login.register"), color=LINK_BLUE, weight=ft.FontWeight.BOLD, size=13),
                    on_click=lambda _: self.router.navigate("/register")
                )
            ], alignment=ft.MainAxisAlignment.CENTER),

        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

        return AuthLayout.wrap(
            form_content=login_form_content,
            hero_title_key="auth.login.hero_title",
            hero_subtitle_key="auth.login.hero_subtitle"
        )
