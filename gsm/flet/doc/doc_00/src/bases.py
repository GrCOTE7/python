import flet as ft
import sys
from pathlib import Path
from datetime import datetime


tools_path = Path(__file__).parent.parent.parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
import time


def main(page: ft.Page):

    now = datetime.now()
    thetime = f"{now.hour: >2}:{now.minute:0>2}:{now.second:0>2}"
    # sys.stdout.write(f"\r{thetime}")

    lesns = [i for i in range(9)]

    print(", ".join(map(str, lesns)))

    name_field = ft.TextField(label="Your name")
    output_name = ft.Text()

    def show_name(e):
        if name_field.value:
            output_name.value = f"Hello, {name_field.value}!"
            page.update()

    for i in range(10):
        page.controls.append(ft.Text(f"Line {nf(i,0): >3}"))
        print(page.controls)
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)
    page.add(
        ft.Row(
            controls=[
                ft.Text("A"),
                ft.Text(", ".join(map(str, lesns))),
                ft.Text("C"),
            ]
        ),
        ft.Row(
            controls=[
                name_field,
                ft.ElevatedButton(text="Say my name!", on_click=show_name),
            ]
        ),
        output_name,
        ft.Column(
            [
                ft.Text("Hello, World!"),
                ft.ElevatedButton(text="Click me", on_click=lambda _: print("Clicked")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    print(thetime)
    # exit()


ft.app(main)
