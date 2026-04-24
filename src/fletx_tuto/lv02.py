import flet as ft
from fletx.core import FletXController, FletXPage, RxInt
from fletx.decorators import obx
from fletx.utils.context import AppContext


class CounterController(FletXController):
    def __init__(self) -> None:
        super().__init__()
        self.count = RxInt(0)

    def increment(self) -> None:
        self.count.set(self.count.value + 1)


class CounterPage(FletXPage):
    def __init__(self) -> None:
        super().__init__(padding=12)
        self.ctrl = CounterController()
        self.counter_text = obx(
            lambda: ft.Text(
                value=f"Count: {self.ctrl.count.value}",
                size=24,
                weight=ft.FontWeight.BOLD,
            )
        )
        self._build_page()

    def build(self) -> ft.Control:
        return ft.Column(
            controls=[
                self.counter_text(),
                ft.ElevatedButton(
                    text="Increment",
                    on_click=lambda _: self.ctrl.increment(),
                ),
            ],
            tight=True,
        )


def main(page: ft.Page) -> None:
    page.title = "FletX Tuto - lv02"
    AppContext.initialize(page)
    page.add(CounterPage())
