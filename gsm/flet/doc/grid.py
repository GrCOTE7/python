from ctypes import alignment
import flet as ft
from theTime import theTime as tt
import os

import flet_lottie as fl


os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):
    rs = ft.Row(
        wrap=True,
        scroll="always",
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    for i in range(5000):
        rs.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", color="black"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER_100,
                border=ft.border.all(1, ft.Colors.AMBER_200),
                border_radius=ft.border_radius.all(5),
            ),
        ),

    # Utilisation d'un Container principal pour forcer le centrage
    centered_container = ft.Container(
        content=rs, alignment=ft.alignment.center, expand=True
    )

    page.add(centered_container)
    page.update()

    print(tt(), page.route)


ft.app(main)
