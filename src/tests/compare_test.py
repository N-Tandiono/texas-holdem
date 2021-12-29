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
import compare

def test_pair():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Hearts", "1")]
    assert(compare.has_pair(cards))

def test_two_pair():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Hearts", "1"), Card("Diamonds", "2")]
    assert(compare.has_two_pair(cards))
    
def test_house():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Spades", "2"), Card("Hearts", "1"), Card("Diamonds", "2")]
    assert(compare.has_full_house(cards))

def test_four_kind():
    cards = [Card("Diamonds", "1"), Card("Spades", "1"), Card("Spades", "1"), Card("Hearts", "1")]
    assert(compare.has_four_kind(cards))

def test_fail_four_kind():
    cards = [Card("Diamonds", "1"), Card("Spades", "1"), Card("Spades", "1"), Card("Hearts", "2")]
    assert(compare.has_four_kind(cards) == False)

def test_flush():
    cards = [Card("Diamonds", "1"), Card("Diamonds", "2"), Card("Diamonds", "2"), Card("Diamonds", "1"), Card("Diamonds", "2")]
    assert(compare.has_flush(cards))

def test_two_pair():
    cards = [Card("Diamonds", "1"), Card("Spades", "2"), Card("Spades", "1"), Card("Hearts", "Ace"), Card("Diamonds", "Ace")]
    assert(compare.has_two_pair(cards))

def test_royal_flush():
    cards = [Card("Diamonds", "10"), Card("Diamonds", "Jack"), Card("Diamonds", "Queen"), Card("Diamonds", "King"), Card("Diamonds", "Ace")]
    assert(compare.has_royal_flush(cards))

def test_royal_flush_mixed():
    cards = [Card("Diamonds", "Queen"), Card("Diamonds", "Ace"), Card("Diamonds", "10"), Card("Diamonds", "King"), Card("Diamonds", "Jack")]
    assert(compare.has_royal_flush(cards))

def test_straight_low():
    cards = [Card("Spades", "Ace"), Card("Diamonds", "2"), Card("Hearts", "3"), Card("Diamonds", "4"), Card("Diamonds", "5")]
    assert(compare.has_straight(cards))

def test_straight_mid():
    cards = [Card("Spades", "7"), Card("Diamonds", "8"), Card("Hearts", "9"), Card("Diamonds", "10"), Card("Diamonds", "Jack")]
    assert(compare.has_straight(cards))

def test_straight_high():
    cards = [Card("Spades", "10"), Card("Diamonds", "Jack"), Card("Hearts", "Queen"), Card("Diamonds", "King"), Card("Diamonds", "Ace")]
    assert(compare.has_straight(cards))

def test_straight_flush():
    cards = [Card("Spades", "10"), Card("Spades", "Jack"), Card("Spades", "Queen"), Card("Spades", "King"), Card("Spades", "Ace")]
    assert(compare.has_straight_flush(cards))

def test_fail_straight_wrapped():
    cards = [Card("Spades", "King"), Card("Diamonds", "Ace"), Card("Hearts", "2"), Card("Diamonds", "3"), Card("Diamonds", "4")]
    assert(compare.has_straight(cards) == False)

def test_fail_straight_wrapped_2():
    cards = [Card("Spades", "Jack"), Card("Diamonds", "Queen"), Card("Hearts", "King"), Card("Diamonds", "Ace"), Card("Diamonds", "2")]
    assert(compare.has_straight(cards) == False)

def test_fail_straight__flush_wrapped():
    cards = [Card("Spades", "King"), Card("Spades", "Ace"), Card("Spades", "2"), Card("Spades", "3"), Card("Spades", "4")]
    assert(compare.has_straight(cards) == False)
    