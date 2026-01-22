import flet as ft
from core.state import AppState
from core.router import Router
from core.logger import Logger
from configs.app_config import APP_TITLE

class FletingApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = APP_TITLE
        self.router = Router(self.page)
        self.startup_locked = True # Lock to prevent route hijacking on start

    def run(self):
        # Initial device state
        AppState.update_device(self.page.width)
        
        # Subscribe to events
        self.page.on_resized = self.on_resize
        self.page.on_route_change = self.on_route_change
        
        # Start navigation: STRICTLY force Login on startup as requested
        Logger.info("App starting: Forcing navigation to /login")
        self.page.route = "/login"
        self.router.navigate("/login")
        self.startup_locked = False # Unlock after first forced navigation
        self.page.update()

    def on_route_change(self, e):
        # If we are starting up, ignore browser-initiated route changes
        if self.startup_locked:
            return
            
        Logger.info(f"Route changed to: {self.page.route}")
        self.router.navigate(self.page.route)

    def on_resize(self, e):
        AppState.update_device(self.page.width)
        # Update current view if needed
        self.page.update()
