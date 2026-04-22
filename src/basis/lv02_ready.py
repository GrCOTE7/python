from dataclasses import field
import flet as ft


@ft.control
class Ready(ft.Container):

    def init(self):

        self.bgcolor = "#252525"
        self.width = 350
        self.height = 200
        self.border_radius = ft.BorderRadius.all(12)
        self.padding = 20

        self._value: int = 123

        self.content = ft.Text(str(self._value), color=ft.Colors.WHITE, size=20)


def main(page: ft.Page):
    page.title = "Quick essai"

    myTest = Ready()
    page.add(myTest)


if __name__ == "__main__":

    ft.run(main)
