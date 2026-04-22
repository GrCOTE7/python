import flet as ft
import tools.screen_utils as screen_utils

import datetime

# disable auto-update globally
ft.context.disable_auto_update()

# Dans main.py, NE PAS FAIRE :
# from importlib import import_module
# example_btn = import_module("examples.02_btn")
# → FOnctionne en local, pas ds APK


def main(page: ft.Page, name: str):

    def button_click(e):
        page.controls.append(ft.Text("Clicked!"))
        page.update()  # must call explicitly since auto-update is off

    page.controls.append(ft.Button("Click me", on_click=button_click))
    page.update()

    page.add(ft.Text(name, size=18, color=ft.Colors.GREEN_ACCENT_400))
    print(datetime.datetime.now().strftime("%H:%M:%S"), ">")
