import flet as ft
from typing import Sequence


def lesson_header_controls(lesson: int) -> list[ft.Control]:
    return [
        ft.Row(
            controls=[
                ft.Text(
                    "Routing & Navigation",
                    weight=ft.FontWeight.BOLD,
                    size=18,
                ),
                ft.Container(expand=True),
                ft.Text(
                    f"Leçon # {lesson}",
                    size=16,
                    italic=True,
                    color=ft.Colors.CYAN_300,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ft.Divider(color=ft.Colors.RED_ACCENT_400, thickness=2, height=0),
        ft.Divider(color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2, height=0),
    ]


def build_lv26_et_plus_view(
    *,
    route: str,
    appbar_title: str,
    lesson: int = 26,
    body_controls: Sequence[ft.Control] | None = None,
) -> ft.View:
    controls = [
        *lesson_header_controls(lesson=lesson),
        ft.AppBar(
            title=ft.Text(appbar_title),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            toolbar_height=68,
        ),
        *(list(body_controls) if body_controls else []),
    ]

    return ft.View(
        route=route,
        controls=[ft.SafeArea(content=ft.Column(controls=controls))],
    )
