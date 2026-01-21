import flet as ft
from core.state import AppState
from core.router import Router
from configs.app_config import APP_TITLE

class FletingApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = APP_TITLE
        self.router = Router(self.page)

    def run(self):
        # Initial device state
        AppState.update_device(self.page.width)
        
        # Subscribe to events
        self.page.on_resized = self.on_resize
        self.page.on_route_change = self.on_route_change
        
        # Start navigation to the actual current route
        self.router.navigate(self.page.route)
        self.page.update()

    def on_route_change(self, e):
        Logger.info(f"Route changed to: {self.page.route}")
        self.router.navigate(self.page.route)

    def on_resize(self, e):
        AppState.update_device(self.page.width)
        # Update current view if needed
        self.page.update()
