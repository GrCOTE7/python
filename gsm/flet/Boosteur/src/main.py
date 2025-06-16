import flet as ft
from datetime import datetime as dt
import time


def boosteurIsBack(txt='Boosteur v2 is back!'):

        return ft.Container(
            padding=5,
            content=ft.Stack(
                # height=100,
                # width=400,
                controls=[
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                txt,
                                ft.TextStyle(
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        color=ft.Colors.BLUE_700,
                                        stroke_width=6,
                                        stroke_join=ft.StrokeJoin.ROUND,
                                        style=ft.PaintingStyle.STROKE,
                                    ),
                                ),
                            ),
                        ],
                    ),
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                txt,
                                ft.TextStyle(
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_300,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )


def main(page: ft.Page):

    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    now = dt.now()
    theTime = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"

    BOOSTER_VERSION = "Boosteur_v0.00.01"

    page.title = f"{theTime} - {BOOSTER_VERSION}"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.bgcolor = FG
    # page.add(ft.Text("Hello, world!"))

    # t = ft.Text(
    #     " Booteur is coming... ",
    #     size=48,
    #     color=PINK,
    #     weight="bold",
    #     bgcolor=BG,
    # )

    t = boosteurIsBack(BOOSTER_VERSION)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(t)

    print(theTime, page.route)


ft.app(target=main)
