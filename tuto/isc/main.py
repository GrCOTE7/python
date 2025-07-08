import flet as ft
import gc7_positioned as gc7


def main(page: ft.Page):
    arr = list(range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]
    
    gc7.position(page)

    txt = "Ready."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)
    arr2 = arr[:5:3]
    print('arr', arr, "→", arr[:5])
    print('arr2', arr2)

ft.app(target=main)
