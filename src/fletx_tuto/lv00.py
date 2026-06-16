import flet as ft
from typing import cast


def main(page: ft.Page) -> None:
    page.title = "#00 | FletX Tuto"

    count = 0
    txt = ft.Text(value=f"LV00\n\nCount: {count}", size=24, weight=ft.FontWeight.BOLD)

    def increment(_: ft.Event[ft.Button]) -> None:
        nonlocal count
        count += 1
        txt.value = f"LV00\n\nCount: {count}"
        page.update()

    page.add(
        ft.Column(
            controls=cast(
                list[ft.Control],
                [
                    txt,
                    ft.Button("Increment", on_click=increment),
                ],
            ),
            tight=True,
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, host="127.0.0.1", port=8550)
