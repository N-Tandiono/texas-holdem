'''
tests for compare.py
'''

import sys, os

# Adjust directory to src
curr = os.path.dirname(__file__)
src = '..'
sys.path.insert(0, os.path.abspath(os.path.join(curr, src)))

import pytest
from card import Card
from compare import find_highest_combination

def test_high():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Hearts", "3")]
    assert(find_highest_combination(cards) == "High Card")

def test_pair():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Hearts", "1")]
    assert(find_highest_combination(cards) == "Pair")

def test_two_pair():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Hearts", "1"), Card("Diamonds", "2")]
    assert(find_highest_combination(cards) == "Two Pair")
    