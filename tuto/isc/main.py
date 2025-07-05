import flet as ft
import gc7_positioned as gc7


def main(page: ft.Page):
    gc7.position(page)

    txt = "Ready."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)


ft.app(target=main)
