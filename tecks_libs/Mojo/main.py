import flet as ft
import tools.gc7 as gc7
from time import time
from tools.gc7 import EC, EW, ER, EN

def app(page: ft.Page):
    gc7.flet_window_position(page)

    txt = "Ready."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)

    print(gc7.theTime())


def main():
    n = 1_000_000
    lang = "python"
    line = f"1, 2, 3, \b\b... J'ai compté jusqu'à {EC}{gc7.nf(n,0):>17}{EN} en {EW}{lang[0].upper() + lang[1:].lower():^6}{EN} → ⏱️ : {ER}{123.35:>6.2f}{EN} secondes"

    print(line)

    length = gc7.rawStrLength(line)[0]
    print ('-'*length)


if __name__ == "__main__":
    main()

ft.app(target=app)
