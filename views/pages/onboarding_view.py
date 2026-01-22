import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.auth_service import AuthService
from core.profile_service import ProfileService
from core.currency_service import CurrencyService, Currency
from core.logger import Logger
from models.user_profile import UserProfile
from views.components.auth_layout import AuthLayout

class OnboardingView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        # Force light mode for onboarding to ensure maximum legibility
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.auth_service = AuthService()
        self.profile_service = ProfileService()
        self.currency_service = CurrencyService()
        
        # Ensure we start with the current global language
        self.selected_language = I18n._current_lang
        
        self.currencies = []
        
        self._init_controls()
    def _build_dropdown(self, label_key, hint_key=None, options=[], value=None, on_change=None):
        dropdown = ft.Dropdown(
            options=options,
            value=value,
            border_radius=8,
            border_color=ft.Colors.GREY_600,
            border_width=2,
            focused_border_color=UserTheme.PRIMARY,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            height=55,
            width=370,
            text_size=16,
            content_padding=ft.padding.symmetric(horizontal=15),
        )
        try:
            dropdown.menu_style = ft.MenuStyle(
                bgcolor=ft.Colors.WHITE,
            )
        except:
            pass # Fallback for older versions if MenuStyle fails

        # Force styles for extreme legibility
        dropdown.text_style = ft.TextStyle(
            size=16, 
            color=ft.Colors.BLACK, 
            weight=ft.FontWeight.BOLD
        )
        dropdown.icon_color = ft.Colors.BLACK
        
        if hint_key:
            dropdown.hint_text = I18n.t(hint_key)
            dropdown.hint_style = ft.TextStyle(color=ft.Colors.GREY_600)
            
        if on_change:
            dropdown.on_change = on_change

        return ft.Column([
            ft.Text(I18n.t(label_key), weight=ft.FontWeight.W_800, size=13, color=ft.Colors.BLACK),
            dropdown
        ], spacing=6)

    def _init_controls(self):
        # UI controls
        self.language_container = self._build_dropdown(
            label_key="onboarding.language_label",
            options=[
                ft.dropdown.Option("es", "Español"),
                ft.dropdown.Option("en", "English"),
                ft.dropdown.Option("pt", "Português"),
            ],
            value=self.selected_language,
            on_change=self.handle_language_change
        )
        self.language_dropdown = self.language_container.controls[1]
        
        self.currency_container = self._build_dropdown(
            label_key="onboarding.currency_label",
            hint_key="onboarding.currency_hint",
            options=[]
        )
        self.currency_dropdown = self.currency_container.controls[1]
        
        self.error_text = ft.Text("", color=ft.Colors.RED_400, size=12, weight=ft.FontWeight.W_500)
        self.loading_indicator = ft.ProgressBar(visible=False, color=UserTheme.PRIMARY)

    def handle_language_change(self, e):
        lang = self.language_dropdown.value
        I18n.set_language(lang)
        self.selected_language = lang
        # Refresh the entire view to update translations
        self.router.navigate("/onboarding")

    def handle_submit(self, e):
        if not self.currency_dropdown.value:
            self.error_text.value = I18n.t("validation.selection_required")
            self.page.update()
            return

        self.error_text.value = ""
        self.loading_indicator.visible = True
        self.page.update()

        user_res = self.auth_service.get_current_user()
        if user_res and user_res.user:
            # Update profile with selected currency
            # and reuse full_name from auth metadata if available
            full_name = user_res.user.user_metadata.get("full_name", "User")
            
            # Force read directly from the UI control which is the ultimate source of user intent
            selected_currency = self.currency_dropdown.value
            selected_lang = self.language_dropdown.value
            
            # Update I18n immediately to ensure it matches selection
            if selected_lang and selected_lang != I18n._current_lang:
                I18n.set_language(selected_lang)

            profile = UserProfile(
                id=user_res.user.id,
                full_name=full_name,
                currency_code=selected_currency,
                preferred_language=selected_lang
            )
            
            Logger.info(f"Submitting onboarding for {user_res.user.id}: Currency={profile.currency_code}, Lang={profile.preferred_language}")
            
            res = self.profile_service.update_profile(profile)
            if res["success"]:
                Logger.info(f"Onboarding update success. Data response: {res['data']}")
                # Ensure language is applied globally before navigating
                I18n.set_language(selected_lang) # Use the verified local variable
                # Success! Navigate to dashboard
                self.router.navigate("/")
                return 
            else:
                self.error_text.value = f"Error: {res['error']}"
        else:
            self.error_text.value = "Session expired. Please login again."
        
        self.loading_indicator.visible = False
        self.page.update()

    def _load_currencies(self):
        res = self.currency_service.get_all_currencies()
        if res["success"]:
            self.currencies = res["currencies"]
            self.currency_dropdown.options = [
                ft.dropdown.Option(c.code, str(c)) for c in self.currencies
            ]
            if self.currencies:
                self.currency_dropdown.value = self.currencies[0].code
            self.page.update()

    def render(self):
        # 1. Fetch user name for personalization
        user_res = self.auth_service.get_current_user()
        full_name = "User"
        if user_res and user_res.user:
            full_name = user_res.user.user_metadata.get("full_name", "User")

        # 2. Load data if not already loaded
        if not self.currency_dropdown.options:
            self._load_currencies()

        form_content = ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.AUTO_AWESOME_ROUNDED, color=UserTheme.PRIMARY, size=50),
                ft.Container(height=10),
                ft.Text(I18n.t("onboarding.title").replace("{name}", full_name), 
                        size=28, weight=ft.FontWeight.W_800, color=UserTheme.SECONDARY, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20), # Space after welcome (as requested)
                ft.Text(I18n.t("onboarding.subtitle"), size=15, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
                
                ft.Container(height=40), # More room before inputs
                
                self.language_container,
                ft.Container(height=15),
                self.currency_container,
                
                ft.Container(height=20),
                self.error_text,
                self.loading_indicator,
                ft.Container(height=20),
                
                ft.ElevatedButton(
                    I18n.t("onboarding.submit"),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor=UserTheme.PRIMARY,
                        color=UserTheme.SECONDARY
                    ),
                    width=float("inf"),
                    height=55,
                    on_click=self.handle_submit
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, spacing=0),
            expand=True,
            alignment=ft.alignment.Alignment(0, 0) # Center both vertically and horizontally
        )

        # 3. Return Wrapped Layout
        return AuthLayout.wrap(
            form_content=form_content,
            hero_title_key="onboarding.hero_title",
            hero_subtitle_key="onboarding.hero_subtitle"
        )
