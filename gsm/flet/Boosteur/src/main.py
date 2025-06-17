import flet as ft
from datetime import datetime as dt

# import tomllib

# # Définir le chemin du fichier pyproject.toml
# import os

# print(os.getcwd())
# file_path = "./Boosteur/pyproject.toml"  # Modifie avec ton chemin réel
# with open(file_path, "rb") as f:
#     config = tomllib.load(f)

# version = config.get("project", {}).get("version", "Version non définie")
# print(f"Version du projet : {version}")
APP_NAME = 'Boosteur'
BOOSTER_VERSION = "0.00.001"


def boosteurIsBack(txt=APP_NAME):

    return ft.Container(
        padding=-10,
        content=ft.Stack(
            # height=100,
            # width=400,
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            txt,
                            ft.TextStyle(
                                size=70,
                                weight=ft.FontWeight.BOLD,
                                foreground=ft.Paint(
                                    color=ft.Colors.BLUE_700,
                                    stroke_width=5,
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
                                size=70,
                                weight=ft.FontWeight.BOLD,
                                # color=ft.Colors.GREY_300,
                                color=ft.Colors.PINK_500,
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

    page.title = f"{theTime} - {APP_NAME} v_{BOOSTER_VERSION}"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = BG

    # page.add(ft.Text("Hello, world!"))

    # t = ft.Text(
    #     " Booteur is coming... ",
    #     size=48,
    #     color=PINK,
    #     weight="bold",
    #     bgcolor=BG,
    # )

    t = boosteurIsBack()
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(t, ft.Text("v_" + BOOSTER_VERSION, color=FWG))

    print(theTime, page.route)


ft.app(target=main)
