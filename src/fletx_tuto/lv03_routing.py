import sys
import asyncio
from pathlib import Path

import flet as ft
from pathspec import GitIgnoreSpec

# Ensure this file's directory is on sys.path so 'views' is always found.
sys.path.insert(0, str(Path(__file__).parent))

from fletx.app import FletXApp
from fletx.core.routing.router import FletXRouter
from fletx.core.routing.models import NavigationMode
from fletx.navigation import ModuleRouter
from fletx.decorators import register_router

from views.home import HomePage
from views.about import AboutPage


@register_router  # type: ignore
class RoutingDemoRouter(ModuleRouter):
    name = "routing_demo"
    base_path = "/"
    is_root = True
    routes = [
        {"path": "/", "component": HomePage},
        {"path": "/about", "component": AboutPage},
    ]
    sub_routers = []


async def main(page: ft.Page) -> None:
    app = FletXApp(
        title="FletX Routing Demo",
        initial_route="/",
        navigation_mode=NavigationMode.HYBRID,
        debug=True,
    )
    await app.create_async_main_handler()(page)
    # Ensure first view is rendered when embedded in an existing Flet loop.
    router = FletXRouter.get_instance()
    nav_result = await router.navigate(app.initial_route, replace=True)

    # Some embedded setups keep an empty active view/control stack.
    # Fallback to a direct HomePage render to avoid a blank window.
    active_view_empty = bool(page.views) and not page.views[-1].controls
    no_visible_content = (not page.controls and not page.views) or active_view_empty
    if nav_result.value != "success" or no_visible_content:
        home = HomePage()
        home._build_page()
        page.clean()
        page.add(home)
        page.update()


def run_app(page: ft.Page | None = None) -> None:
    # Standalone launch: create Flet page loop via ft.run.
    if page is None:
        ft.run(main)
        return

    # Embedded launch (called from another app already holding a page).
    asyncio.create_task(main(page))


if __name__ == "__main__":
    run_app()
