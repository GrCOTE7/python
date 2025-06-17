import flet as ft
from theTime import theTime as tt


def main(page: ft.Page):
    page.add(
        ft.Text(
            spans=[
                ft.TextSpan(
                    "Greetings, planet!",
                    ft.TextStyle(
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (0, 20), (150, 20), [ft.Colors.RED, ft.Colors.YELLOW]
                            )
                        ),
                    ),
                ),
            ],
        )
    )

    print(tt(), page.route)


ft.app(main)
