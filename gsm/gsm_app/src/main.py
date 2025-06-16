import flet as ft
from numpy import spacing

# from matplotlib.hatch import HorizontalHatch


def main(page: ft.Page):

    page.title = "Photos"
    page.scroll = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    layout = ft.Row(spacing=5, wrap=True)
    label = ft.Text("From Lionel")

    for i in range(20):
        layout.controls.append(
            ft.Container(
                ft.Image(
                    src=f"https://picsum.photos/350/350?{i}",
                    border_radius=ft.border_radius.all(10),
                    width=150,
                    height=150,
                )
            )
        )

    page.add(label, layout)


ft.app(main)
