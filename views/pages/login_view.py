import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.validator import Validator
from core.auth_service import AuthService
from core.logger import Logger
from core.profile_service import ProfileService
from views.components.auth_layout import AuthLayout

class LoginView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        self.auth_service = AuthService()
        self.profile_service = ProfileService()
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
        
        # 1. Validation
        if not Validator.is_valid_email(email):
            self._show_error(I18n.t("validation.email_invalid"))
            return
            
        if not password:
            self._show_error(I18n.t("auth.login.password_hint"))
            return

        # 2. Loading state
        self._set_loading(True)

        # 3. Call Auth Service
        res = self.auth_service.sign_in(email, password)
        
        if res["success"]:
            # 4. Check if it's the first time (Phase 5 logic)
            user = res["user"]
            profile_res = self.profile_service.get_profile(user.id)
            
            if profile_res["success"] and profile_res["profile"].currency_code:
                # 4.1 Apply stored language preference
                stored_lang = profile_res["profile"].preferred_language
                if stored_lang:
                    I18n.set_language(stored_lang)
                    Logger.info(f"Applied language preference: {stored_lang}")

                # User already completed onboarding
                Logger.info(f"User {user.id} logged in. Profile complete. Going to Dashboard.")
                self.router.navigate("/")
            else:
                # First time or incomplete profile -> Go to onboarding
                Logger.info(f"User {user.id} logged in. Profile incomplete. Going to Onboarding.")
                self.router.navigate("/onboarding")
        else:
            # Check for unconfirmed email specifically
            error_msg = res["error"].lower()
            if "email not confirmed" in error_msg:
                self.handle_unconfirmed_login(email)
                return

            self._set_loading(False)
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

    def _map_auth_error(self, error_str):
        """Maps Supabase login errors to localized strings."""
        err = error_str.lower()
        if "invalid login credentials" in err or "invalid_credentials" in err:
            return I18n.t("auth.login.errors.invalid") 
        if "email not confirmed" in err:
            return I18n.t("auth.login.errors.email_not_confirmed")
        return I18n.t("errors.generic")

    def render(self):
        
        def on_hover(e):
            if not e.control.disabled:
                e.control.scale = 1.02 if e.data == "true" else 1.0
                e.control.update()

        # Build Submit Button
        self.submit_button = ft.ElevatedButton(
            content=ft.Row([self.submit_button_text, self.progress_ring], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor={ft.ControlState.HOVERED: UserTheme.PRIMARY, ft.ControlState.DEFAULT: UserTheme.PRIMARY},
            ),
            width=float("inf"),
            height=55,
            on_hover=on_hover,
            on_click=self.handle_login
        )

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
                    content=ft.Text(I18n.t("auth.login.forgot_password"), color=UserTheme.LINK, size=12),
                    on_click=lambda _: self.router.navigate("/construction")
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            self.error_text,
            ft.Container(height=25),

            self.submit_button,

            ft.Container(height=45),

            # Footer
            ft.Row([
                ft.Text(I18n.t("auth.login.no_account"), color=ft.Colors.GREY_500, size=13),
                ft.TextButton(
                    content=ft.Text(I18n.t("auth.login.register"), color=UserTheme.LINK, weight=ft.FontWeight.BOLD, size=13),
                    on_click=lambda _: self.router.navigate("/register")
                )
            ], alignment=ft.MainAxisAlignment.CENTER),

        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

        # Wrap in a container to allow swapping content for feedback views
        self.form_container = ft.Container(content=login_form_content)

        return AuthLayout.wrap(
            form_content=self.form_container,
            hero_title_key="auth.login.hero_title",
            hero_subtitle_key="auth.login.hero_subtitle"
        )

    def handle_unconfirmed_login(self, email):
        """
        Handles the specific case where login fails due to unverified email.
        Automatically triggers a resend and shows a feedback view.
        """
        Logger.info(f"Triggering smart resend for unverified email: {email}")
        
        # 1. Show intermediate loading state
        self._set_loading(False) # Stop the button spinner
        self.form_container.content = ft.Column([
            ft.ProgressRing(color=UserTheme.PRIMARY),
            ft.Container(height=20),
            ft.Text(I18n.t("auth.login.verification_required.action"), size=16, color=UserTheme.SECONDARY)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.page.update()

        # 2. Trigger Resend with correct redirect URL
        redirect_url = self._sanitize_redirect_url()
        res = self.auth_service.resend_verification_email(email, redirect_to=redirect_url)

        # 3. Show Result View
        if res["success"]:
            self.show_verification_sent_view(email)
        else:
            # Fallback to login form with error if resend failed
            self.restore_login_form()
            self._show_error(f"Error resending email: {res.get('error')}")
            
    def _sanitize_redirect_url(self):
        url = self.page.url
        if not url: return None
        url = url.replace("ws://", "http://").replace("wss://", "https://")
        sanitized = url.split("#")[0].split("?")[0]
        Logger.info(f"Sanitized redirect URL for Supabase (Login): {sanitized}")
        return sanitized

    def show_verification_sent_view(self, email):
        success_content = ft.Column([
            ft.Container(ft.Icon(ft.Icons.MARK_EMAIL_UNREAD_ROUNDED, color=UserTheme.PRIMARY, size=80), margin=ft.margin.only(bottom=20)),
            ft.Text(I18n.t("auth.login.verification_required.title"), size=32, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY, text_align=ft.TextAlign.CENTER),
            ft.Text(I18n.t("auth.login.verification_required.message").replace("{email}", email), size=16, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            ft.Container(
                content=ft.Text(I18n.t("auth.login.verification_required.success"), size=14, color=ft.Colors.GREEN_700, text_align=ft.TextAlign.CENTER),
                bgcolor=ft.Colors.GREEN_50,
                padding=15,
                border_radius=10,
                border=ft.border.all(1, ft.Colors.GREEN_200)
            ),
            ft.Container(height=40),
            ft.ElevatedButton(
                I18n.t("auth.login.verification_required.back_button"),
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: self.router.navigate("/login"), # Reloads the view
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), bgcolor=UserTheme.PRIMARY, color=UserTheme.SECONDARY),
                height=50
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)

        self.form_container.content = success_content
        self.page.update()

    def restore_login_form(self):
        # Simply reload the page to restore state, easiest way
        self.router.navigate("/login")
