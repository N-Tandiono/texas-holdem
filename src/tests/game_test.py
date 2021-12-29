'''
tests for game.py
'''

import sys, os

# Adjust directory to src
curr = os.path.dirname(__file__)
src = '..'
sys.path.insert(0, os.path.abspath(os.path.join(curr, src)))

import pytest
from game import Game
from player.player import Player
from player.human_player import HumanPlayer

from card import Card
from constants import rank

@pytest.fixture()
def setup():
    return Game()

def test_cards_players_sample(setup):
    '''
    Players compared
    '''
    a = HumanPlayer("Player 1", 1000)
    a.give_card(Card("Diamonds", "8"))
    a.give_card(Card("Spades", "9"))
    
    b = HumanPlayer("Player 2", 1000)
    b.give_card(Card("Diamonds", "5"))
    b.give_card(Card("Diamonds", "10"))

    setup._table.attach(a)
    setup._table.attach(b)
    
    setup._table.add_table_cards(Card("Diamonds", "5"))
    setup._table.add_table_cards(Card("Spades", "6"))
    setup._table.add_table_cards(Card("Spades", "7"))
    setup._table.add_table_cards(Card("Hearts", "King"))
    setup._table.add_table_cards(Card("Diamonds", "Ace"))
    
    assert(setup.reveal() == {rank.STRAIGHT: [a], rank.PAIR: [b]})
