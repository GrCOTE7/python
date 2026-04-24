import flet as ft
import sys
from pathlib import Path
from typing import cast

# Allow running this file directly: `python src/fletx_tuto/lv01.py`
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from fletx_mini_local.core import RxInt
from fletx_mini_local.decorators import obx


def main(page: ft.Page) -> None:
    page.title = "#01 | FletX Tuto"

    count = RxInt(0)
    counter_text = obx(
        lambda: ft.Text(
            value=f"LV01\n\nCount: {count.value}",
            size=24,
            weight=ft.FontWeight.BOLD,
        )
    )

    def increment(_: ft.Event[ft.Button]) -> None:
        count.set(count.value + 1)

    page.add(
        ft.Column(
            controls=cast(
                list[ft.Control],
                [
                    counter_text(),
                    ft.Button("Incarement", on_click=increment),
                ],
            ),
            tight=True,
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, host="127.0.0.1", port=8551)
