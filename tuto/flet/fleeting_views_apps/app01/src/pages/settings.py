import flet as ft


def settings_init(fv):
    settings_button = ft.TextButton(
        icon=ft.Icons.DATA_ARRAY,
        text="Get Settings data!",
        on_click=lambda e: print(fv.get_params()),
    )
    setting_container = ft.Container(
        content=ft.Text("I'm the text of the Settings page", size=40),
    )

    fv.append("settings", [setting_container, settings_button])
