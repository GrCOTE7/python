import flet as ft

# Use of GestureDetector with on_pan_update event for dragging card
# Absolute positioning of controls within stack


def main(page: ft.Page):
    page.title = "Drag a card | Solitaire #31"
    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.local_delta.y)
        e.control.left = max(0, e.control.left + e.local_delta.x)
        e.control.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_update=drag,
        left=0,
        top=0,
        content=ft.Container(
            border_radius=ft.BorderRadius.all(4),
            bgcolor=ft.Colors.GREEN,
            width=70,
            height=100,
        ),
    )

    page.add(ft.Stack(controls=[card], width=1000, height=500))


if __name__ == "__main__":
    ft.run(main)
