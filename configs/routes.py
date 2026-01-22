# Route mapping for the application
# Format: "route_path": "module_path_for_lazy_loading"

ROUTE_MAP = {
    "/": "views.pages.dashboard_view.DashboardView",
    "/login": "views.pages.login_view.LoginView",
    "/register": "views.pages.register_view.RegisterView",
    "/onboarding": "views.pages.onboarding_view.OnboardingView",
    "/dashboard": "views.pages.dashboard_view.DashboardView",
    "/construction": "views.pages.construction_view.ConstructionView"
}
