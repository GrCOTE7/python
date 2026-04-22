import flet as ft
from examples.lv36_slot import Slot
from examples.lv36_card import Card

SOLITAIRE_WIDTH = 392  # 976
SOLITAIRE_HEIGHT = 500


class Solitaire(ft.Stack):

    def __init__(self):
        super().__init__()

        self.controls = [ft.Container(expand=True, bgcolor=ft.Colors.TRANSPARENT)]
        self.slots = []
        self.cards = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    def create_card_deck(self):
        card1 = Card(self, color="GREEN")
        card2 = Card(self, color="YELLOW")
        self.cards = [card1, card2]

    def create_slots(self):
        self.slots.append(Slot(top=0, left=0))
        self.slots.append(Slot(top=0, left=190))
        self.slots.append(Slot(top=0, left=280))
        self.controls.extend(self.slots)
        self.update()

    def deal_cards(self):
        self.controls.extend(self.cards)
        for card in self.cards:
            card.place(self.slots[0])
        self.update()
