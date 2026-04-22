import flet as ft

from examples.lv39_solitaire import Solitaire
from tools.screen_utils import gc7_rules as gc7


def main(page: ft.Page):

    gc7(page, width=710)
    title = "Rule - Solitaire #39"
    page.title = title.replace("-", "|")
    page.add(ft.Text(title, size=18, weight=ft.FontWeight.BOLD))
    page.bgcolor = ft.Colors.GREEN_900

    solitaire = Solitaire()
    page.add(solitaire)


if __name__ == "__main__":
    ft.run(main, assets_dir="images")
