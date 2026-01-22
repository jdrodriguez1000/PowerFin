import flet as ft
from core.i18n import I18n

class SummaryCard(ft.Container):
    def __init__(self, title_key, value_text_control, icon, icon_color="#0F172A"):
        super().__init__()
        
        # Build subtitle key
        subtitle_key = f"{title_key}_subtitle"
        subtitle_val = I18n.t(subtitle_key)
        subtitle_text = subtitle_val if subtitle_val != f"[{subtitle_key}]" else ""

        # Adjust value text control style for white background
        value_text_control.color = "#0F172A"
        value_text_control.size = 28
        value_text_control.weight = ft.FontWeight.W_800

        self.content = ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Icon(icon, color=icon_color, size=22, opacity=0.9),
                    padding=12,
                    bgcolor=ft.Colors.with_opacity(0.08, icon_color),
                    border_radius=12,
                ),
            ], alignment=ft.MainAxisAlignment.START),
            ft.Container(height=25),
            ft.Text(I18n.t(title_key).upper(), color="#94A3B8", size=11, weight=ft.FontWeight.W_700),
            ft.Container(height=8),
            value_text_control,
            ft.Container(height=8),
            ft.Text(subtitle_text, color="#CBD5E1", size=11, weight=ft.FontWeight.W_400),
        ], spacing=0)
        
        self.padding = 25
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 24
        self.expand = True
        self.shadow = ft.BoxShadow(
            blur_radius=30,
            color=ft.Colors.with_opacity(0.04, ft.Colors.BLACK),
            offset=ft.Offset(0, 10),
        )
