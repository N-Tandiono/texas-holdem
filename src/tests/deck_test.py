'''
tests for deck.py
'''

import sys, os

# Adjust directory to src
curr = os.path.dirname(__file__)
src = '..'
sys.path.insert(0, os.path.abspath(os.path.join(curr, src)))

import pytest
from game import Game
from compare import is_card_in

@pytest.fixture()
def setup():
    return Game()

def test_52_cards(setup):
    assert(len(setup._deck.cards_in_deck) == 52)

def test_13_hearts(setup):
    hearts = []
    for card in setup._deck.cards_in_deck:
        if card.suit == "Hearts":
            hearts.append(card)
    assert(len(hearts) == 13)

def test_13_clubs(setup):
    clubs = []
    for card in setup._deck.cards_in_deck:
        if card.suit == "Clubs":
            clubs.append(card)
    assert(len(clubs) == 13)

def test_13_diamonds(setup):
    diamonds = []
    for card in setup._deck.cards_in_deck:
        if card.suit == "Diamonds":
            diamonds.append(card)
    assert(len(diamonds) == 13)

def test_13_spades(setup):
    spades = []
    for card in setup._deck.cards_in_deck:
        if card.suit == "Spades":
            spades.append(card)
    assert(len(spades) == 13)

def test_cards_unique(setup):
    list = []
    for card in setup._deck.cards_in_deck:
        assert(is_card_in(card, list) == False)
        list.append(card)