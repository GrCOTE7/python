import flet as ft

from .template import build_lv26_et_plus_view


def build_root_view(open_setting, lesson: int = 26) -> ft.View:
    return build_lv26_et_plus_view(
        route="/",
        appbar_title="Flet App",
        lesson=lesson,
        body_controls=[
            ft.Button("Go to Settings", on_click=open_setting),
        ],
    )
