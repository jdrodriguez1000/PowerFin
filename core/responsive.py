import flet as ft
from core.state import AppState

class Responsive:
    @staticmethod
    def get_layout(mobile=None, tablet=None, desktop=None):
        device = AppState.device
        if device == "mobile":
            return mobile or tablet or desktop
        elif device == "tablet":
            return tablet or desktop or mobile
        else:
            return desktop or tablet or mobile
