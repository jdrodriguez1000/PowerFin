import flet as ft

class AppState:
    device = "desktop"  # mobile, tablet, desktop
    language = "es"
    is_navigating = False
    user = None  # To store Supabase user session

    @classmethod
    def update_device(cls, width):
        if width < 600:
            cls.device = "mobile"
        elif width < 1200:
            cls.device = "tablet"
        else:
            cls.device = "desktop"
