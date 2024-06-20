"""Player and Hand."""

from typing import List

from .card import Card

# 2do Finir ce tuto https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable/7188702-structurez-une-application-avec-le-pattern-d-architecture-mvc

class Hand(list):
    """Player hand."""

    def append(self, object):
        """Append a card."""
        if not isinstance(object, Card):
            return ValueError("Vous ne pouvez ajouter que des cartes !")
        return super().append(object)


class Player:
    """Player."""

    def __init__(self, name):
        """Has a name and a hand."""
        self.name = name
        self.hand: List[Card] = Hand()
