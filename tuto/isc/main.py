import flet as ft
import tools.gc7_positioned as gc7
import tutos as tutos

def main(page: ft.Page):

    gc7.position(page)

    txt = "Ready."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)

# def tutos():
#     # tuto_tupple.tupples_tuto()
#     pass


if __name__ == "__main__":

    print("→" * 102, 'MAIN SCRIPT', '→'*3)
    tutos.main()
    print("←" * 118)

# ft.app(target=main)
