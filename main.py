import flet as ft
from core.app import FletingApp
from core.logger import Logger

def main(page: ft.Page):
    Logger.setup()
    Logger.info("Starting PowerFin...")
    
    app = FletingApp(page)
    app.run()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
