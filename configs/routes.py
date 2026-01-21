# Route mapping for the application
# Format: "route_path": "module_path_for_lazy_loading"

ROUTE_MAP = {
    "/": "views.pages.login_view.LoginView",
    "/login": "views.pages.login_view.LoginView",
    "/construction": "views.pages.construction_view.ConstructionView"
}
