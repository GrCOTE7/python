import flet as ft
from theTime import theTime as tt

import flet_lottie as fl

def main(page: ft.Page):
    page.title = "Drag and Drop example"
    
    def drag_will_accept(e):
        e.control.content.border = ft.border.all(
            2, ft.Colors.BLACK45 if e.data == "true" else ft.Colors.RED
        )
        e.control.update()

    def drag_accept(e: ft.DragTargetEvent):
        src = page.get_control(f"{e.src_id}")
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.border = None
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Draggable(
                            group="color",
                            content=ft.Container(
                                width=50,
                                height=50,
                                bgcolor=ft.Colors.CYAN,
                                border_radius=5,
                            ),
                            content_feedback=ft.Container(
                                width=20,
                                height=20,
                                bgcolor=ft.Colors.CYAN,
                                border_radius=3,
                            ),
                        ),
                        ft.Draggable(
                            group="color",
                            content=ft.Container(
                                width=50,
                                height=50,
                                bgcolor=ft.Colors.YELLOW,
                                border_radius=5,
                            ),
                        ),
                        ft.Draggable(
                            group="color",
                            content=ft.Container(
                                width=50,
                                height=50,
                                bgcolor=ft.Colors.GREEN,
                                border_radius=5,
                            ),
                        ),
                    ]
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="color",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.BLUE_GREY_100,
                        border_radius=5,
                    ),
                    on_will_accept=drag_will_accept,
                    on_accept=drag_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )

    print(tt(), page.route)


ft.app(main)
