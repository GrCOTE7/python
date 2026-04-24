import flet as ft


def main(page: ft.Page) -> None:
    page.title = "FletX Tuto - lv01"

    count = 0
    txt = ft.Text(value=f"Count: {count}", size=24, weight=ft.FontWeight.BOLD)

    def increment(_: ft.ControlEvent) -> None:
        nonlocal count
        count += 1
        txt.value = f"Count: {count}"
        page.update()

    page.add(
        ft.Column(
            controls=[
                txt,
                ft.ElevatedButton("Increment", on_click=increment),
            ],
            tight=True,
        )
    )
