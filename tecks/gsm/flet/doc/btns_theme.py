import flet as ft
from theTime import theTime as tt

import flet_lottie as fl


def main(page: ft.Page):
    # page.bgcolor = ft.Colors.GREY_200  # Pour mieux voir les éléments

    btns = ft.Row(
        [
            ft.Container(
                content=ft.Text("Non clickable"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                width=150,
                height=150,
                border_radius=10,
                border=ft.border.all(5, ft.Colors.ON_PRIMARY_CONTAINER),
            ),
            ft.Container(
                content=ft.Text("Clickable without Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.GREEN_200,
                width=150,
                height=150,
                border_radius=10,
                on_click=lambda e: print("Clickable without Ink clicked!"),
            ),
            ft.Container(
                content=ft.Text("Clickable with Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.CYAN_200,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable with Ink clicked!"),
            ),
            ft.Container(
                content=ft.Text("Clickable transparent with Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable transparent with Ink clicked!"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    floating_button = ft.Container(
        content=ft.ElevatedButton(
            text="Change Background",
            color={
                ft.ControlState.HOVERED: ft.Colors.RED,
                ft.ControlState.FOCUSED: ft.Colors.BLUE,
                ft.ControlState.DEFAULT: ft.Colors.BLACK,
            },
            bgcolor=ft.Colors.RED_50,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=12, weight=ft.FontWeight.W_700),
                bgcolor={
                    ft.ControlState.FOCUSED: ft.Colors.PINK_200,
                    "": ft.Colors.YELLOW,
                },
                # padding={ft.ControlState.HOVERED: 20},
                overlay_color=ft.Colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(3, ft.Colors.BLUE),
                    ft.ControlState.HOVERED: ft.BorderSide(1, ft.Colors.BLUE),
                },
                shape={
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=10),
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=4),
                },
                # padding=ft.Padding(50,0,50,0)
            ),
            tooltip="Change THEME MODE",
            on_click=lambda e: change_themeMode(),
            width=150,
        ),
        right=20,
        bottom=20,
    )

    def change_themeMode():
        ptm = page.theme_mode

        page.theme_mode = (
            ft.ThemeMode.DARK if ptm == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )

        floating_button.content.text = "Re-change Background"

        page.update()
        print(tt(), ptm)

    page.add(
        ft.Stack(
            [
                ft.Column(
                    [btns],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                floating_button,
            ],
            expand=True,
        )
    )

    print(tt(), page.route)


ft.app(main)
