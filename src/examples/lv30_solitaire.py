import flet as ft
from pathlib import Path


def main(page: ft.Page):
    page.title = "Tap a card | Solitaire #30"
    def on_card_tap(e: ft.TapEvent):
        if isinstance(card.content, ft.Container):
            print(f"Tap {card.content.bgcolor}")

    card = ft.GestureDetector(
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),
        on_tap=on_card_tap,
    )

    page.add(ft.Stack(controls=[card], width=1000, height=500))


if __name__ == "__main__":
    ft.run(main)
