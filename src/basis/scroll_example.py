from re import A

import flet as ft
import datetime, time
from typing import cast

from wcwidth import wrap
from tools.screen_utils import gc7_rules as gc7


def main(page: ft.Page):

    # from examples.lv06_todo_simple import todo_list as todo6
    # todo6(page)

    # from examples.lv08_todo import todo_list as todo8
    # todo8(page)

    # from devs.lv00_dev import dev as dev
    # dev(page)

    page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=cast(
                list[ft.Control],
                [
                    ft.Text(
                        f"Exemple ligne {i}",
                        size=24,
                        color=ft.Colors.RED_ACCENT_200,
                        weight=ft.FontWeight.BOLD,
                    )
                    for i in range(1, 80)
                ],
            ),
            scroll=ft.ScrollMode.AUTO,
        )
    )


if __name__ == "__main__":

    ft.run(main)
