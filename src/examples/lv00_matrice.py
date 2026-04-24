import flet as ft


@ft.control
class Matrice(ft.Column):
    def __init__(self):
        self.title = ft.Text("Matrice Ready.", size=24)
        self.controls = [self.title]


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#151515"

    page.add(Matrice())


if __name__ == "__main__":

    ft.run(main)
