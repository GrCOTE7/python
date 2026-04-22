from dataclasses import field

import flet as ft


@ft.control
class NombreX(ft.Container):
    def init(self):
        self._values: dict[str, int] = {"x": 0}

        self.bgcolor = "#333333"
        self.width = 350
        self.height = 200
        self.border_radius = ft.BorderRadius.all(12)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="Nombre X", color=ft.Colors.WHITE, size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

def game(page: ft.Page):
    page.title = "Jeu du Nombre Mystérieux"

    # create application instances
    game = NombreX()
    # add application's root control to the page
    page.add(game)


if __name__ == "__main__":

    ft.run(game)
