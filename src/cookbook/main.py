import flet as ft
from typing import Callable

from tools.screen_utils import gc7_rules as gc7
from .lvAll import *


def main(page: ft.Page):
    print(f"Dans src/main → {page.route = }")
    title = "Cookbook"
    # gc7(page, defaultColors=False)
    page.title = title.replace("-", "|")
    # gc7(page, mode='LIGHT')
    page.add(
        ft.Column(
            spacing=0,
            controls=[
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
                ft.Divider(color=ft.Colors.RED_ACCENT_400, thickness=2, height=7),
                ft.Divider(
                    color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2, height=7
                ),
            ],
        )
    )
    # page.scroll = ft.ScrollMode.AUTO
    page.scroll = None
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    # page.spacing = 20
    # page.bgcolor = ft.Colors.GREEN_900

    lvs = []
    renderers: list[Callable[[], object]] = []

    # lvs.append(Lv00("Salut !"))  # Simple class with a custom text
    # lvs.append(Lv00())  # Simple class with a custom text
    #
    # lvs.append(Lv01())  # Form with a text field and a button
    # lvs.append(Lv02())  # 3 blocs in a row with different expand values and colors
    # lvs.append(Lv03())  # A counter
    # lvs.append(Lv04())  # 3 blocs in a stack with different expand values and colors
    # lvs.append(Lv05())  # Row, Column, Container, Safearea, Stack
    # lvs.append(Lv06())  # ResponsiveRow
    # lvs.append(Lv07())  # Shadow & Action - Joli btn
    # lvs.append(Lv08())  # A container in another
    #
    # lvs.append(Lv09(page))  # Fonts
    #
    # lvs.append(Lv10())  # .env
    #
    # lvs.append(Lv11(page))  # Theming
    #
    # lvs.append(Lv12(page))  # Imperative CRUD
    # renderers.append(lambda: Lv13(page))  # Declarative CRUD (uses page.render)
    # renderers.append(lambda: Lv14(page))  # Declarative CRUD (uses page.render) + Dynamic Edit Btn
    #
    # lvs.append(Lv15())  # Drag & Drop
    # lvs.append(Lv16(page)) # Keyboard Shotcuts
    #
    # lvs.append(Lv17(page))  # Async Msgs
    # lvs.append(Lv18())  # Async Countdowns
    #
    # lvs.append(Lv19())  # Large list
    # lvs.append(Lv20())  # Large list - Simplier Chargement par lots)
    # lvs.append(Lv21())  # Large list (Illimited ListView() + batch loading)
    # lvs.append(Lv22())  # Large list (Infinite ListView())
    #
    # lvs.append(Lv23())  # Simple PubSUb
    # lvs.append(Lv24())  # SubProcess
    #
    # lvs.append(Lv25(page))  # Routing & Navigation
    # lvs.append(Lv26(page))  # Idem Lv25 mais page dans fichiers séparés
    # lvs.append(Lv27(page))  # Confirm pop (pour back)
    #
    # lvs.append(Lv28(page))  # Simple drawer (Menu Burger)
    # lvs.append(Lv29(page))  # Simple drawer + Navigation
    # lvs.append(Lv30(page))  # Route templates (parameterized routes)
    #
    # gc7(page, mode="LIGHT", width=700)
    # gc7(page, width=700)
    page.adaptive = True  # Optimize iOS et Android platforms
    # lvs.append(Lv31(page))  # Adaptive apps
    #
    lvs.append(Lv32())  # DataTable sortable

    # gc7(page, mode='LIGHT')
    # gc7(page, width=500)

    if renderers:
        # Keep declarative mode isolated from page.add/page.controls flow.
        page.clean()
        renderers[-1]()
    elif lvs:
        # page.add(*lvs)
        page.add(lvs[-1])

    elif len(page.controls) < 2:
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                margin=ft.Margin.only(top=25),
                controls=[
                    ft.Text(
                        "No content.",
                        size=30,
                        color=ft.Colors.RED_ACCENT_200,
                        weight=ft.FontWeight.BOLD,
                    )
                ],
            )
        )

    # lvs.append(Lv99())  # 3 blocs in a stack with different expand values and colors
    # page.add(lvs[-1])


if __name__ == "__main__":
    ft.run(main)
