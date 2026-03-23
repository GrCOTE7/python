import flet as ft

n_containers = 1


def add_container(fv):
    global n_containers
    container = ft.Container(content=ft.Text(f"Container {n_containers}"))
    n_containers += 1
    fv.append("settings", container)


def settings_init(fv):
    settings_button = ft.TextButton(
        icon=ft.Icons.DATA_ARRAY,
        text="Get Settings data!",
        on_click=lambda e: print(fv.get_params()),
    )
    add_container_button = ft.TextButton(
        icon=ft.Icons.ADD, text="ADD CONTAINER", on_click=lambda e: add_container(fv)
    )
    setting_container = ft.Container(
        content=ft.Text("I'm the text of the Settings page", size=40),
    )

    fv.append("settings", [setting_container, add_container_button, settings_button])
