import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.auth_service import AuthService
import re

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
        name = self.name_field.controls[1].value
        email = self.email_field.controls[1].value
        password = self.password_field.controls[1].value
        confirm = self.confirm_password_field.controls[1].value

        # --- Basic Validation ---
        if not name or len(name) < 3:
            self.error_text.value = "Ingresa tu nombre completo (mín. 3 caracteres)"
            self.page.update()
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.error_text.value = "Ingresa un correo electrónico válido"
            self.page.update()
            return

        if len(password) < 8:
            self.error_text.value = "La contraseña debe tener al menos 8 caracteres"
            self.page.update()
            return

        if password != confirm:
            self.error_text.value = "Las contraseñas no coinciden"
            self.page.update()
            return

        self.error_text.value = ""
        self.page.update()

        # --- Call Auth Service ---
        res = self.auth_service.sign_up(email, password, name)
        
        if res["success"]:
            # Success: Redirect or show message
            # For now, let's redirect to login or show success
            self.page.snack_bar = ft.SnackBar(ft.Text("¡Registro exitoso! Revisa tu correo."), bgcolor=ft.Colors.GREEN_600)
            self.page.snack_bar.open = True
            self.router.navigate("/login")
        else:
            self.error_text.value = f"Error: {res['error']}"
            self.page.update()

    def render(self):
        LINK_BLUE = "#0D47A1"
        
        # --- LEFT SIDE: THE HERO IMAGE ---
        hero_side = ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLACK,
            content=ft.Stack([
                ft.Image(
                    src="/imgs/login_bg.png",
                    fit=ft.BoxFit.COVER,
                    expand=True,
                ),
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.BOTTOM_CENTER,
                        end=ft.Alignment.TOP_CENTER,
                        colors=["#D5000000", "#44000000"]
                    ),
                    expand=True,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Container(
                                content=ft.Icon(ft.Icons.MONETIZATION_ON_ROUNDED, color=UserTheme.PRIMARY, size=32),
                                bgcolor=ft.Colors.WHITE,
                                padding=8,
                                border_radius=50,
                            ),
                            ft.Text("PowerFin", size=26, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                        ], spacing=15),
                        ft.Column([
                            ft.Text(
                                I18n.t("auth.register.hero_title"), 
                                size=44, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, width=400,
                            ),
                            ft.Text(
                                I18n.t("auth.register.hero_subtitle"), 
                                size=18, color=ft.Colors.WHITE, opacity=0.8,
                            ),
                        ], spacing=10),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=60, margin=ft.margin.only(bottom=40), expand=True,
                )
            ], expand=True),
        )

        # --- RIGHT SIDE: THE REGISTER FORM ---
        def on_hover(e):
            e.control.scale = 1.02 if e.data == "true" else 1.0
            e.control.update()

        register_form = ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            alignment=ft.Alignment.CENTER,
            content=ft.Container(
                width=420,
                padding=ft.padding.symmetric(vertical=20),
                content=ft.Column([
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

                    # Register button
                    ft.ElevatedButton(
                        content=ft.Text(I18n.t("auth.register.submit"), size=16, weight=ft.FontWeight.BOLD, color=UserTheme.SECONDARY),
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
                        on_click=self.handle_register
                    ),

                    ft.Container(height=30),

                    # Footer
                    ft.Row([
                        ft.Text(I18n.t("auth.register.already_have_account"), color=ft.Colors.GREY_500, size=13),
                        ft.TextButton(
                            content=ft.Text(I18n.t("auth.register.login"), color=LINK_BLUE, weight=ft.FontWeight.BOLD, size=13),
                            on_click=lambda _: self.router.navigate("/login")
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),

                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
            ),
        )

        return ft.Row([hero_side, register_form], expand=True, spacing=0)
