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

def test_chips_after_round(setup):
    '''
    Players compared chips are game scenario
    '''
    a = HumanPlayer("Player 1", 1000)
    a.give_card(Card("Diamonds", "8"))
    a.give_card(Card("Spades", "9"))
    
    b = HumanPlayer("Player 2", 1000)
    b.give_card(Card("Diamonds", "5"))
    b.give_card(Card("Diamonds", "10"))

    a._chips -= 100
    b._chips -= 100

    a._round_bet += 100
    b._round_bet += 100

    setup._table.pot = 200

    setup._table.attach(a)
    setup._table.attach(b)
    
    setup._table.add_table_cards(Card("Diamonds", "5"))
    setup._table.add_table_cards(Card("Spades", "6"))
    setup._table.add_table_cards(Card("Spades", "7"))
    setup._table.add_table_cards(Card("Hearts", "King"))
    setup._table.add_table_cards(Card("Diamonds", "Ace"))
    
    setup.reveal()

    assert(setup._table.pot == 0)
    assert(a._chips == 1100)
    assert(b._chips == 900)
    assert(a._chips + b._chips == 2000)

def test_chips_after_round(setup):
    '''
    Players compared chips are game scenario
    '''
    a = HumanPlayer("Player 1", 1000)
    a.give_card(Card("Diamonds", "8"))
    a.give_card(Card("Spades", "9"))
    
    b = HumanPlayer("Player 2", 1000)
    b.give_card(Card("Diamonds", "5"))
    b.give_card(Card("Diamonds", "10"))

    a._chips -= 100
    b._chips -= 100

    a._round_bet += 100
    b._round_bet += 100

    setup._table.pot = 200

    setup._table.attach(a)
    setup._table.attach(b)
    
    setup._table.add_table_cards(Card("Diamonds", "5"))
    setup._table.add_table_cards(Card("Spades", "6"))
    setup._table.add_table_cards(Card("Spades", "7"))
    setup._table.add_table_cards(Card("Hearts", "King"))
    setup._table.add_table_cards(Card("Diamonds", "Ace"))
    
    setup.reveal()

    assert(setup._table.pot == 0)
    assert(a._chips == 1100)
    assert(b._chips == 900)
    assert(a._chips + b._chips == 2000)

def test_chips_after_round_higher_card(setup):
    '''
    Players compared chips are game scenario
    '''
    a = HumanPlayer("Player 1", 1000)
    a.give_card(Card("Diamonds", "10"))
    a.give_card(Card("Spades", "4"))
    
    b = HumanPlayer("Player 2", 1000)
    b.give_card(Card("Diamonds", "4"))
    b.give_card(Card("Diamonds", "3"))

    a._chips -= 100
    b._chips -= 100

    a._round_bet += 100
    b._round_bet += 100

    setup._table.pot = 200

    setup._table.attach(a)
    setup._table.attach(b)
    
    setup._table.add_table_cards(Card("Diamonds", "Ace"))
    setup._table.add_table_cards(Card("Spades", "King"))
    setup._table.add_table_cards(Card("Spades", "Queen"))
    setup._table.add_table_cards(Card("Hearts", "2"))
    setup._table.add_table_cards(Card("Diamonds", "6"))
    
    setup.reveal()

    assert(setup._table.pot == 0)
    assert(a._chips == 1100)
    assert(b._chips == 900)
    assert(a._chips + b._chips == 2000)
