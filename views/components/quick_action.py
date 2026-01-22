import flet as ft
from core.i18n import I18n
from core.theme import UserTheme
from core.logger import Logger

class QuickAction(ft.Container):
    def __init__(self, icon, label_key, color, on_click=None):
        super().__init__()
        
        self.content = ft.Column([
            ft.Container(
                content=ft.Icon(icon, color=color, size=28),
                bgcolor=ft.Colors.with_opacity(0.1, color),
                padding=15,
                border_radius=15,
            ),
            ft.Text(I18n.t(label_key), size=12, weight=ft.FontWeight.W_600, color=UserTheme.SECONDARY, text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        
        self.on_click = on_click if on_click else lambda _: Logger.info(f"Quick action: {label_key}")
        self.padding = 10
        self.ink = True
        self.border_radius = 15
        self.width = 100 # Fixed width for grid consistency
