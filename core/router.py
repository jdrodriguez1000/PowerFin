import flet as ft
import importlib
from configs.routes import ROUTE_MAP
from core.logger import Logger

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_route = None

    def navigate(self, route_path):
        if route_path not in ROUTE_MAP:
            Logger.error(f"Route not found: {route_path}")
            # Could show a 404 view here
            return

        module_path = ROUTE_MAP[route_path]
        Logger.info(f"Navigating to {route_path} -> {module_path}")
        
        try:
            # Dynamic loading of the view
            parts = module_path.split(".")
            class_name = parts[-1]
            module_name = ".".join(parts[:-1])
            
            module = importlib.import_module(module_name)
            view_class = getattr(module, class_name)
            
            # Reset page controls
            self.page.controls.clear()
            
            # Instantiate and render the view
            view_instance = view_class(self.page, self)
            content = view_instance.render()
            
            self.page.add(content)
            self.current_route = route_path
            self.page.update()
            
        except Exception as e:
            Logger.error(f"Error loading view for {route_path}: {str(e)}")
            # Handle error (fallback view)
