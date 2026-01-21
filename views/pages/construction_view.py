import flet as ft
from core.i18n import I18n
from core.theme import UserTheme

class ConstructionView:
    def __init__(self, page: ft.Page, router):
        self.page = page
        self.router = router
        self.page.bgcolor = UserTheme.BACKGROUND

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.CONSTRUCTION_ROUNDED, size=100, color=ft.Colors.ORANGE_400),
                    ft.Text(
                        I18n.t("construction.title"), 
                        size=32, 
                        weight=ft.FontWeight.BOLD,
                        color=UserTheme.SECONDARY,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        I18n.t("construction.message"), 
                        size=18, 
                        text_align=ft.TextAlign.CENTER,
                        color=UserTheme.TEXT_SECONDARY
                    ),
                    ft.Container(height=30),
                    ft.TextButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ARROW_BACK, color=UserTheme.SECONDARY),
                                ft.Text(I18n.t("construction.back"), color=UserTheme.SECONDARY, weight=ft.FontWeight.BOLD)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            tight=True
                        ),
                        on_click=lambda _: self.router.navigate("/")
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.Alignment(0, 0),
            padding=20,
            bgcolor=UserTheme.BACKGROUND
        )
