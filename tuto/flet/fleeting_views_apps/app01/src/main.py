import flet as ft
import FleetingViews as fvs

from pages.home import home_init
from pages.settings import settings_init

# Ref: https://www.youtube.com/watch?v=eCoyLg9uHiY&ab_channel=BrunoArellano

def main(page: ft.Page):

    page.padding = ft.padding.all(10)
    # page.padding = ft.Padding(20, 10, 20, 10)

    page_snack_bar = ft.SnackBar(
        content=ft.Text("", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
        action="Accept!",
        duration=5000,
        bgcolor=ft.Colors.WHITE,
        action_color=ft.Colors.RED,
    )

    # Assign the SnackBar to the page
    page.snack_bar = page_snack_bar

    appbar = ft.AppBar(
        actions=[
            ft.IconButton(
                icon=ft.Icons.HOME,
                on_click=lambda e: fv.view_go("home?id=23&login=false"),
            ),
            ft.IconButton(
                icon=ft.Icons.SETTINGS,
                on_click=lambda e: fv.view_go("settings?id=23&login=true"),
            ),
            ft.PopupMenuButton(
                items=[ft.PopupMenuItem(text="Settings"), ft.PopupMenuItem(text="Help")]
            ),
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MENU),
        ]
    )

    view_definitions = {
        "home": {
            "bgcolor": ft.Colors.BLUE_GREY,
            "vertical_alignment": ft.MainAxisAlignment.CENTER,
            "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
            "appbar": appbar,
        },
        "settings": {
            "bgcolor": ft.Colors.AMBER_900,
            "vertical_alignment": ft.MainAxisAlignment.CENTER,
            "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
            "appbar": appbar,
        },
    }

    def my_callback_hook(view, params):
        page.snack_bar.content.value = f"View changed to: {view} Params: {params}"
        page.open(page_snack_bar)
        # page.snack_bar = page_snack_bar
        # page.snack_bar.open = True

    fv = fvs.create_views(view_definitions = view_definitions, page=page)
    fv.on_view_change = my_callback_hook

    home_init(fv)
    settings_init(fv)

ft.app(main)
