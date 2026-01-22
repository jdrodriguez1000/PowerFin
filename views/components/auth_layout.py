import flet as ft
from core.i18n import I18n
from core.theme import UserTheme

class AuthLayout:
    @staticmethod
    def wrap(form_content, hero_title_key, hero_subtitle_key):
        """
        Wraps a form content into the common Auth split-screen layout.
        """
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
                                I18n.t(hero_title_key), 
                                size=44, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, width=400,
                            ),
                            ft.Text(
                                I18n.t(hero_subtitle_key), 
                                size=18, color=ft.Colors.WHITE, opacity=0.8,
                            ),
                        ], spacing=10),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=60, margin=ft.margin.only(bottom=40), expand=True,
                )
            ], expand=True),
        )

        # --- RIGHT SIDE: THE FORM CONTAINER ---
        form_panel = ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            alignment=ft.alignment.Alignment(0, 0),
            content=ft.Container(
                width=420,
                content=form_content
            )
        )

        return ft.Row([hero_side, form_panel], expand=True, spacing=0)
