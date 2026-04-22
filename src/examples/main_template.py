import flet as ft
from examples.lv_02_btn import main as btn2
from tools.screen_utils import gc7_rules as gc7


def main(page: ft.Page):
    name: str = "Ready"
    gc7(page, name)

    btn2(page, name)


ft.run(main)
