from algo2017 import vvv
import flet as ft
from datetime import datetime as dt


def main(page: ft.Page):
    page.title = "uuu".capitalize()

    page.add(ft.Text("Hello World 21 !"))

    now = dt.now()
    tt = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    
    print("Ready.", tt)
    vvv.print_message()


ft.app(main)
