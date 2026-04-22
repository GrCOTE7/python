import flet as ft
from pathlib import Path

_CC = {"BLUE": "#0000ff", "WHITE": "#ffffff", "RED": "#ff0000"}  # cc = card colors


def card(i):
    card_w = 70
    ccc = list(_CC.keys())  # ["BLUE", "WHITE", "RED"]

    card = ft.GestureDetector(
        left=i * 35, # 100
        top=i* 35, # 0
        content=ft.Container(bgcolor=_CC[ccc[i]], width=card_w, height=100),
        on_tap=lambda e: print(f"Tap {ccc[i]}"),
    )
    return card


# ❌ cf voir dessous
def main(page: ft.Page):

    cards = []
    for i in range(3):
        cards.append(card(i))


    page.add(ft.Stack(controls=cards, width=1000, height=500))


if __name__ == "__main__":
    ft.run(main)
