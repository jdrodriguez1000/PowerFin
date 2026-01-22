import flet as ft
import importlib
from configs.routes import ROUTE_MAP
from core.logger import Logger
from core.auth_service import AuthService
from core.profile_service import ProfileService

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_route = None
        self.auth_service = AuthService()
        self.profile_service = ProfileService()

    def navigate(self, route_path):
        # 1. Sanitize route
        clean_path = route_path.split("#")[0].split("?")[0]
        if not clean_path or clean_path == "":
            clean_path = "/"
            
        # 2. Navigation Guards (Simplified)
        # We allow every route to be requested. The logic of where to go
        # is now handled manually in the Login button and App startup.
        pass

        # 3. Standard Navigation
        if clean_path not in ROUTE_MAP:
            Logger.error(f"Route not found: {clean_path} (Original: {route_path})")
            if not self.current_route:
                clean_path = "/"
            else:
                return

        module_path = ROUTE_MAP[clean_path]
        Logger.info(f"Navigating to {clean_path} -> {module_path}")
        
        try:
            parts = module_path.split(".")
            class_name = parts[-1]
            module_name = ".".join(parts[:-1])
            
            module = importlib.import_module(module_name)
            view_class = getattr(module, class_name)
            
            self.page.controls.clear()
            
            view_instance = view_class(self.page, self)
            content = view_instance.render()
            
            self.page.add(content)
            self.current_route = clean_path
            self.page.update()
            
        except Exception as e:
            Logger.error(f"Error loading view for {route_path}: {str(e)}")
