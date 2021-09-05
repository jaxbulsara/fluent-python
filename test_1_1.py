import random

import pytest

from example_1_1 import Card, FrenchDeck


@pytest.fixture
def deck():
    return FrenchDeck()


def test_card():
    beer_card = Card("7", "diamonds")
    assert str(beer_card) == "Card(rank='7', suit='diamonds')"


def test_deck_length(deck: FrenchDeck):
    assert len(deck) == 52


def test_deck_get_item(deck: FrenchDeck):
    assert deck[0] == Card("2", "spades")
    assert deck[-1] == Card("A", "hearts")


def test_deck_random(deck: FrenchDeck):
    assert random.choice(deck) in deck


def test_deck_slicing(deck: FrenchDeck):
    first_three = [
        Card("2", "spades"),
        Card("3", "spades"),
        Card("4", "spades"),
    ]
    assert deck[:3] == first_three

    aces = [
        Card("A", "spades"),
        Card("A", "diamonds"),
        Card("A", "clubs"),
        Card("A", "hearts"),
    ]
    assert deck[12::13] == aces


def test_deck_iteration(deck: FrenchDeck):
    for position, card in enumerate(deck):
        assert card == deck[position]


def test_deck_reversed_iteration(deck: FrenchDeck):
    for position, card in enumerate(reversed(deck)):
        position_from_end = len(deck) - 1 - position
        assert card == deck[position_from_end]


def test_deck_sorting(deck: FrenchDeck):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card: Card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for index, card in enumerate(sorted(deck, key=spades_high, reverse=True)):
        if index == 0:
            assert card == Card("A", "spades")

        if index == len(deck) - 1:
            assert card == Card("2", "clubs")
