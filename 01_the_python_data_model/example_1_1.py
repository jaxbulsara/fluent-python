import collections

Card = collections.namedtuple("Card", ["rank", "suit"])
NUMBERED_CARDS = [str(n) for n in range(2, 11)]
COURT_CARDS = list("JQKA")
CARD_SUITS = "spades diamonds clubs hearts".split()


class FrenchDeck:
    ranks = NUMBERED_CARDS + COURT_CARDS
    suits = CARD_SUITS

    def __init__(self) -> None:
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
