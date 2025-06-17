import flet as ft
from datetime import datetime as dt

def main(page: ft.Page):
    now = dt.now()
    theTime = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"

    t = "Hi!"
    page.add(ft.Text(t))

    print(theTime, page.route)


ft.app(target=main)
