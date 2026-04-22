import flet as ft
from examples.lv36_solitaire  import Solitaire

def main(page: ft.Page):

    title = "POO code - Solitaire #36"
    page.title = title.replace("-", "|")
    page.add(ft.Text(title, size=18, weight=ft.FontWeight.BOLD))
    page.bgcolor = ft.Colors.GREEN_900

    solitaire = Solitaire()
    page.add(solitaire)


if __name__ == "__main__":
    ft.run(main)
