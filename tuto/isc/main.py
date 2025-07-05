import flet as ft
import gc7_positioned as gc7


def main(page: ft.Page):
    gc7.position(page)

    txt = "Ready."
    t = ft.Text(txt, size=30)
    page.add(t)


ft.app(target=main)
