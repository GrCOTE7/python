import flet as ft

# Using Container for slot where the card should be dropped
# on_pan_start event for the card: remember position of card to bounce it back on_pan_end of needed.
# on_pan_end: check if card is in proximity of the slot and either place it to the slot or return to original position (bounce back).
# Solitaire class created for holding original position coordinates


class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0


def main(page: ft.Page):

    page.title = "Drag on slot or back | Solitaire #33"

    def place(card, slot):
        """place card to the slot"""
        card.top = slot.top
        card.left = slot.left
        print("Placed!")

    def bounce_back(game, card):
        card.top = game.start_top
        card.left = game.start_left
        print("← Bounce back!")
        page.update()

    def start_drag(e: ft.DragStartEvent):
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left
        e.control.update()

    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.local_delta.y)
        e.control.left = max(0, e.control.left + e.local_delta.x)
        e.control.update()

    def drop(e: ft.DragEndEvent):
        if abs(e.control.top - slot.top) < 50 and abs(e.control.left - slot.left) < 35:
            place(e.control, slot)
        else:
            bounce_back(solitaire, e.control)
        e.control.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
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

    solitaire = Solitaire()

    page.add(ft.Stack(controls=[slot, card], width=976, height=500))


if __name__ == "__main__":
    ft.run(main)
