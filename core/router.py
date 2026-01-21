import flet as ft
import importlib
from configs.routes import ROUTE_MAP
from core.logger import Logger

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_route = None

    def navigate(self, route_path):
        # Sanitize route: remove everything after '#' or '?' to handle Supabase redirects
        clean_path = route_path.split("#")[0].split("?")[0]
        
        # If path is empty (just the hash was present) or only "/", default to "/"
        if not clean_path or clean_path == "":
            clean_path = "/"
            
        if clean_path not in ROUTE_MAP:
            Logger.error(f"Route not found: {clean_path} (Original: {route_path})")
            # If not found, stay on current or go to root if nothing loaded
            if not self.current_route:
                clean_path = "/"
            else:
                return

        module_path = ROUTE_MAP[clean_path]
        Logger.info(f"Navigating to {clean_path} -> {module_path}")
        
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
