import flet as ft
import tools.gc7 as gc7


def main(page: ft.Page):
    gc7.flet_window_position(page)

    txt = "Ready."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)

    print(gc7.theTime())

    import exos.maison_des_jeux.courses_avec_les_enfants


ft.app(target=main)
