import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.auth_service import AuthService
from core.logger import Logger
from core.validator import Validator
from views.components.auth_layout import AuthLayout

class RegisterView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        self.auth_service = AuthService()
        self.page.bgcolor = ft.Colors.WHITE
        self.page.padding = 0
        
        # Form Controls
        self.name_field = self._build_textfield(
            label_key="auth.register.name_label",
            hint_key="auth.register.name_hint",
            icon=ft.Icons.PERSON_OUTLINE
        )
        self.email_field = self._build_textfield(
            label_key="auth.register.email_label",
            hint_key="auth.register.email_hint",
            icon=ft.Icons.EMAIL_OUTLINED
        )
        self.password_field = self._build_textfield(
            label_key="auth.register.password_label",
            hint_key="auth.register.password_hint",
            icon=ft.Icons.LOCK_OUTLINE,
            password=True
        )
        self.confirm_password_field = self._build_textfield(
            label_key="auth.register.confirm_password_label",
            hint_key="auth.register.confirm_password_hint",
            icon=ft.Icons.LOCK_RESET,
            password=True
        )
        self.error_text = ft.Text("", color=ft.Colors.RED_400, size=12, weight=ft.FontWeight.W_500)
        
        # Loading state
        self.progress_ring = ft.ProgressRing(width=16, height=16, stroke_width=2, color=UserTheme.SECONDARY, visible=False)
        self.submit_button_text = ft.Text(I18n.t("auth.register.submit"), size=16, weight=ft.FontWeight.BOLD, color=UserTheme.SECONDARY)

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

    def handle_register(self, e):
        # 1. Trim Inputs
        name = self.name_field.controls[1].value.strip()
        email = self.email_field.controls[1].value.strip()
        password = self.password_field.controls[1].value
        confirm = self.confirm_password_field.controls[1].value

        # 2. Basic Validation
        if not Validator.is_valid_name(name):
            self._show_error(I18n.t("validation.name_invalid"))
            return

        if not Validator.is_valid_email(email):
            self._show_error(I18n.t("validation.email_invalid"))
            return

        if not Validator.is_strong_password(password):
            self._show_error(I18n.t("validation.password_short"))
            return

        if password != confirm:
            self._show_error(I18n.t("validation.passwords_mismatch"))
            return

        # 3. Loading State
        self._set_loading(True)
        
        redirect_url = self._sanitize_redirect_url()
        res = self.auth_service.sign_up(email, password, name, redirect_to=redirect_url)
        
        self._set_loading(False)

        if res["success"]:
            self.show_success_view(email)
        else:
            self._show_error(self._map_auth_error(res["error"]))

    def _show_error(self, message):
        self.error_text.value = message
        self.page.update()

    def _set_loading(self, is_loading):
        self.progress_ring.visible = is_loading
        self.submit_button.disabled = is_loading
        self.submit_button_text.visible = not is_loading
        self.error_text.value = ""
        self.page.update()

    def _sanitize_redirect_url(self):
        url = self.page.url
        if not url: return None
        url = url.replace("ws://", "http://").replace("wss://", "https://")
        sanitized = url.split("#")[0].split("?")[0]
        Logger.info(f"Sanitized redirect URL for Supabase: {sanitized}")
        return sanitized

    def _map_auth_error(self, error_str):
        """Maps Supabase errors to localized strings."""
        if "already registered" in error_str.lower() or "already exists" in error_str.lower():
            return I18n.t("auth.register.errors.email_taken")
        return I18n.t("auth.register.errors.unexpected")

    def show_success_view(self, email):
        success_content = ft.Column([
            ft.Container(ft.Icon(ft.Icons.MARK_EMAIL_READ_ROUNDED, color=UserTheme.PRIMARY, size=80), margin=ft.margin.only(bottom=20)),
            ft.Text(I18n.t("auth.register.success.title"), size=32, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY, text_align=ft.TextAlign.CENTER),
            ft.Text(I18n.t("auth.register.success.message").replace("{email}", email), size=16, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            ft.Text(I18n.t("auth.register.success.instruction"), size=14, color=ft.Colors.GREY_500, text_align=ft.TextAlign.CENTER),
            ft.Container(height=40),
            ft.ElevatedButton(
                I18n.t("auth.register.success.login_button"),
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: self.router.navigate("/login"),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), bgcolor=UserTheme.PRIMARY, color=UserTheme.SECONDARY),
                height=50
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)

        self.form_container.content = success_content
        self.page.update()

    def render(self):
        
        def on_hover(e):
            if not e.control.disabled:
                e.control.scale = 1.02 if e.data == "true" else 1.0
                e.control.update()

        # Build Submit Button explicitly to reference it
        self.submit_button = ft.ElevatedButton(
            content=ft.Row([self.submit_button_text, self.progress_ring], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor={ft.ControlState.HOVERED: UserTheme.PRIMARY, ft.ControlState.DEFAULT: UserTheme.PRIMARY},
            ),
            width=float("inf"),
            height=55,
            on_hover=on_hover,
            on_click=self.handle_register
        )

        form_column = ft.Column([
            ft.Column([
                ft.Text(I18n.t("auth.register.title"), size=38, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY),
                ft.Text(I18n.t("auth.register.subtitle"), size=15, color=ft.Colors.GREY_600),
            ], spacing=2),
            ft.Container(height=30),
            self.name_field,
            ft.Container(height=8),
            self.email_field,
            ft.Container(height=8),
            self.password_field,
            ft.Container(height=8),
            self.confirm_password_field,
            ft.Container(height=5),
            self.error_text,
            ft.Container(height=20),
            self.submit_button,
            ft.Container(height=30),
            ft.Row([
                ft.Text(I18n.t("auth.register.already_have_account"), color=ft.Colors.GREY_500, size=13),
                ft.TextButton(
                    content=ft.Text(I18n.t("auth.register.login"), color=UserTheme.LINK, weight=ft.FontWeight.BOLD, size=13),
                    on_click=lambda _: self.router.navigate("/login")
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

        # We wrap the column in a container so we can replace its content later (on success)
        self.form_container = ft.Container(content=form_column)

        return AuthLayout.wrap(
            form_content=self.form_container,
            hero_title_key="auth.register.hero_title",
            hero_subtitle_key="auth.register.hero_subtitle"
        )
