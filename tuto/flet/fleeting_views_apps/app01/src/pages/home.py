import flet as ft


def home_init(fv):
    home_button = ft.TextButton(
        icon=ft.Icons.DATA_ARRAY,
        text="Get Home data!",
        on_click=lambda e: print(fv.get_params()),
    )
    home_container = ft.Container(
        content=ft.Text("I'm the text of the Home page", size=40),
    )

    fv.append("home", [home_container, home_button])
