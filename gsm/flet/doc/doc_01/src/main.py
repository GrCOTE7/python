import flet as ft
import sys
from pathlib import Path
from datetime import datetime


tools_path = Path(__file__).parent.parent.parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
import time


class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.Icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()


def main(page: ft.Page):

    now = datetime.now()
    theTime = f"{now.hour: >2}:{now.minute:0>2}:{now.second:0>2}"
    # sys.stdout.write(f"\r{theTime}")

    page.add(
        Task("Do laundry"),
        Task("Cook diner"),
        )

    print(theTime)
    # exit()


ft.app(main)
