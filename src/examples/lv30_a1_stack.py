import flet as ft
from pathlib import Path


def main(page: ft.Page):
    # card = ft.GestureDetector(
    #     left=0,
    #     top=0,
    #     content=ft.Container(bgcolor=ft.Colors.GREEN, width=100, height=100),
    # )

    # page.add(ft.Stack(controls=[card], width=1000, height=500))

    def getImg(path=None, title="Image Title", position=ft.Alignment(0, -1)):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Stack(
                    width=300,
                    height=300,
                    # alignment=ft.Alignment.CENTER, # Centre absolu
                    alignment=position,
                    controls=[
                        ft.Image(
                            src=str(path) if path else "https://picsum.photos/300/300",
                            # width=300,
                            height=300,
                            fit=ft.BoxFit.CONTAIN,
                        ),
                        ft.Container(
                            expand=True,
                            alignment=position,
                            content=ft.Container(
                                bgcolor=ft.Colors.with_opacity(0.45, ft.Colors.BLACK),
                                border_radius=7,
                                padding=ft.Padding(left=12, top=4, right=12, bottom=6),
                                margin=ft.Margin(top=0, bottom=10),
                                content=ft.Text(
                                    value=title,
                                    color=ft.Colors.WHITE,
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),
                        ),
                    ],
                )
            ],  # Stack fermé, liste controls de Row fermée
        )

    page.add(
        getImg(
            path=str(Path(__file__).parent / "assets" / "images" / "chanteur.jpg"),
            title="Lionel chanteur",
        )
    )
    page.add(getImg(title="Une image au hasard", position=ft.Alignment(0, 1)))

    page.add(
        ft.SafeArea(
            content=ft.Stack(
                margin=ft.Margin.only(top=40, left=150),
                width=40,
                height=40,
                controls=[
                    ft.CircleAvatar(
                        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
                    ),
                    ft.Container(
                        alignment=ft.Alignment.BOTTOM_LEFT,
                        content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5),
                    ),
                ],
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
