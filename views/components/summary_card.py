import flet as ft
from core.i18n import I18n

class SummaryCard(ft.Container):
    def __init__(self, title_key, value_text_control, icon, gradient_colors):
        super().__init__()
        self.gradient_colors = gradient_colors
        
        # Build subtitle key
        subtitle_key = f"{title_key}_subtitle"
        subtitle_val = I18n.t(subtitle_key)
        # Check if translation exists (if it returns the key in brackets, it doesn't exist)
        subtitle_text = subtitle_val if subtitle_val != f"[{subtitle_key}]" else ""

        self.content = ft.Column([
            ft.Row([
                ft.Text(I18n.t(title_key), color=ft.Colors.WHITE70, size=14, weight=ft.FontWeight.W_500),
                ft.Icon(icon, color=ft.Colors.WHITE, size=20, opacity=0.8),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(height=10),
            value_text_control,
            ft.Container(height=5),
            ft.Text(subtitle_text, color=ft.Colors.WHITE60, size=12),
        ], spacing=0)
        
        self.padding = 25
        self.border_radius = 20
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.Alignment(-1, -1),
            end=ft.alignment.Alignment(1, 1),
            colors=gradient_colors,
        )
        self.expand = True
        self.shadow = ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, gradient_colors[0]),
            offset=ft.Offset(0, 8),
        )
