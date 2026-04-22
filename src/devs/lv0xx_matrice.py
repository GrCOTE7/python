import flet as ft

from .templates import rapidTemplate


@ft.control
class rapidTest(ft.Column):
    title_text: str = "RapidTest"

    def init(self):
        self.controls = [
            rapidTemplate(
                title_text=self.title_text,
                detail_items=[
                    "Row Bloc",
                    self.a_row_bloc(),
                    "Column Bloc",
                    self.a_column_bloc(),
                    "Container Bloc",
                    self.a_container_bloc(),
                ],
            )
        ]

    def a_row_bloc(self):
        return ft.Row(
            [
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def a_column_bloc(self):
        return ft.Column(
            [
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def a_container_bloc(self):
        return ft.Container(
            width=250,
            padding=ft.Padding.only(top=10, bottom=30, left=20, right=20),
            bgcolor="black",
            border_radius=12,
            content=ft.Text("Hello"),
        )


def dev(page: ft.Page):
    title = "Dev (Rapid Test)"
    page.title = title

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    page.add(rapidTest(title_text=title))
    page.add(rapidTest())


if __name__ == "__main__":

    ft.run(dev)
