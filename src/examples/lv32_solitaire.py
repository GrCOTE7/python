import flet as ft

# Use of GestureDetector with on_pan_update event for dragging card
# Absolute positioning of controls within stack


def main(page: ft.Page):

    page.title = "Drag to slot | Solitaire #32"

    def drop(e: ft.DragEndEvent):
        if abs(e.control.top - slot.top) < 50 and abs(e.control.left - slot.left) < 35:
            place(e.control, slot)
        e.control.update()

    def place(card, slot):
        """place card to the slot"""
        card.top = slot.top
        card.left = slot.left
        print("Placed!")
        page.update()

    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.local_delta.y)
        e.control.left = max(0, e.control.left + e.local_delta.x)
        e.control.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(
            border_radius=ft.BorderRadius.all(4),
            bgcolor=ft.Colors.GREEN,
            width=70,
            height=100,
        ),
    )

    slot = ft.Container(
        border_radius=ft.BorderRadius.all(4),
        width=70,
        height=100,
        left=250,
        top=0,
        border=ft.Border.all(1),
    )

    page.add(ft.Stack(controls=[slot, card], width=976, height=500))


if __name__ == "__main__":
    ft.run(main)
