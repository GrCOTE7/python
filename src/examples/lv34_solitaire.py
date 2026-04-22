import flet as ft


class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0


def main(page: ft.Page):

    page.title = "More cards | Solitaire #34"

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

    def move_on_top(card, controls):
        """Moves draggable card to the top of the stack"""
        controls.remove(card)
        controls.append(card)
        page.update()

    def start_drag(e: ft.DragStartEvent):
        move_on_top(e.control, controls)
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

    card1 = ft.GestureDetector(
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

    card2 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=90,
        top=0,
        content=ft.Container(
            border_radius=ft.BorderRadius.all(4),
            bgcolor=ft.Colors.YELLOW,
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

    controls = [slot, card1, card2]
    page.add(ft.Stack(controls=controls, width=976, height=500))


if __name__ == "__main__":
    ft.run(main)
