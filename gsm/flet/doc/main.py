import flet as ft
from datetime import datetime as dt
import time


def main(page: ft.Page):

    now = dt.now()
    theTime = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"

    page.title = f"{theTime} - Test GC7"
    page.add(ft.Text("Hello, world!"))

    t = ft.Text("Oki !")
    page.add(t)

    print(theTime, page.route)

ft.app(target=main)
