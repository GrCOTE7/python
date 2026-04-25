"""
MyProject App
None

A FletX application.
Author: Developer
Version: 0.1.0
"""

import asyncio
import sys
from pathlib import Path

# Ensure 'app' package is resolvable from this file's directory.
sys.path.insert(0, str(Path(__file__).parent))

import flet as ft
from fletx.app import FletXApp
from fletx.core.routing.models import NavigationMode
from fletx.core.routing.router import FletXRouter
from app.routes import MyProjectRouter
from app.pages.counter import CounterPage
from app.utils.theme import light_theme, dark_theme


async def main(page: ft.Page):
    """Main entry point for the MyProject application."""

    # Lifecycle Hooks
    async def on_startup(page: ft.Page):
        print("App is running!")

    def on_shutdown(page: ft.Page):
        print("App is closed!")

    # App Configuration
    app = FletXApp(
        title="MyProject",
        initial_route="/",
        debug=True,
        navigation_mode=NavigationMode.HYBRID,
        theme=light_theme,
        dark_theme=dark_theme,
        theme_mode=ft.ThemeMode.SYSTEM,
        window_config={
            "width": 400,
            "height": 810,
            "resizable": True,
            "maximizable": True,
        },
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )

    # Embed dans un Flet existant — initialise FletX sur la page courante
    await app._async_main(page)
    # Laisser la tâche interne de FletXRouter.initialize s'exécuter (T1)
    await asyncio.sleep(0)

    # Fallback : si la navigation T1 n'a rien rendu, forcer l'affichage
    active_view_empty = bool(page.views) and not page.views[-1].controls
    no_content = (not page.controls and not page.views) or active_view_empty
    if no_content:
        home = CounterPage()
        home._build_page()
        page.clean()
        page.add(home)
        page.update()


if __name__ == "__main__":
    # Lancement standalone : ft.app() gère les coros async nativement
    ft.app(target=main)
