import flet as ft
import tools.screen_utils as screen_utils
import datetime

name = "Ready"


def main(page: ft.Page):

    screen_utils.configure_window(page)
    # page.theme_mode = ft.ThemeMode.LIGHT  # Comment to dark
    page.title = "Flet Doc Officielle | " + name

    def button_click(e):
        page.controls.append(ft.Text("Clicked!"))
        # no need to call page.update() — it happens automatically

    page.controls.append(ft.Button("Click me", on_click=button_click))
    # no need to call page.update() here either

    page.add(ft.Text("Ready.", size=28))
    print(datetime.datetime.now().strftime("%H:%M:%S"), ">")


ft.run(main)
