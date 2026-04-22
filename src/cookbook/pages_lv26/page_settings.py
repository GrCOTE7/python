import flet as ft

from .template import build_lv26_et_plus_view


def build_settings_view(open_mail_setting, lesson: int = 26) -> ft.View:
    return build_lv26_et_plus_view(
        route="/settings",
        appbar_title="Settings",
        lesson=lesson,
        body_controls=[
            ft.Text(
                "Settings!",
                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
            ),
            ft.Button(
                content="Go to mail settings",
                on_click=open_mail_setting,
            ),
        ],
    )
