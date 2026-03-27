import flet as ft
import tools.gc7_positioned as gc7

# flet run -d -r .\tecks_libs\flet\main.py

def main(page: ft.Page):

    gc7.position(page)

    txt = "Ready."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)

if __name__ == "__main__":

    print("→" * 102, 'MAIN SCRIPT', '→'*3)
    print("←" * 118)

ft.run(main)
