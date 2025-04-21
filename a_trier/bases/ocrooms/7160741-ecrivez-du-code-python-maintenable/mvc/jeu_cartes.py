"""Jeu de cartes Model"""

SUITS = ("Trèfles", "Piques", "Carreaux", "Coeurs")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "dame",
    "roi",
    "as",
)


class Card:
    """Carte à jouer"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False
        self._ranks_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other: "Card"):
        if self._ranks_score != other._ranks_score:
            return self._ranks_score < other._ranks_score
        return self._suit_score < other._suit_score


c1 = Card("Carreaux", "cinq")
c2 = Card("Carreaux", "roi")
print(c1)
print(c2)
print(c1 < c2)


