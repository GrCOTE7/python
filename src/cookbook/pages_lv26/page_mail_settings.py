import flet as ft

from .template import build_lv26_et_plus_view


def build_mail_settings_view(lesson: int = 26) -> ft.View:
    return build_lv26_et_plus_view(
        route="/settings/mail",
        appbar_title="Mail Settings",
        lesson=lesson,
        body_controls=[ft.Text("Mail settings!")],
    )
