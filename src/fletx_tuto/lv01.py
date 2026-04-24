import flet as ft
from fletx.core import RxInt
from fletx.decorators import obx


def main(page: ft.Page) -> None:
    page.title = "FletX Tuto - lv01"

    count = RxInt(0)

    counter_text = obx(
        lambda: ft.Text(
            value=f"Count: {count.value}",
            size=24,
            weight=ft.FontWeight.BOLD,
        )
    )

    def increment(_: ft.ControlEvent) -> None:
        count.set(count.value + 1)

    page.add(
        ft.Column(
            controls=[
                counter_text(),
                ft.ElevatedButton("Increment", on_click=increment),
            ],
            tight=True,
        )
    )
