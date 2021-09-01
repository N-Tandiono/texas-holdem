from abc import ABC, abstractmethod

from card import Card
from compare import find_highest_combination

class Player(ABC):

    def __init__(self, name: str):
        self._name = name
        self._cards = []
        self._round_bet = 0
        self._chips = 500
        self._role = ""
        self._is_valid_player = True
        self._highest_combination = find_highest_combination(self._cards)

    def update(self, table) -> None:
        # Called on addition of a card to the table.
        
        # Recalculate odds and highest_combination
        self._highest_combination = find_highest_combination(self._cards + table._table_cards)

        # Debug lines below, will create black-box tests in future
        # suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        # vals = ['10', 'Jack', 'Queen', 'King', 'Ace']
        # self._highest_combination = find_highest_combination([Card("Diamonds", "King"),Card("Diamonds", "9"),Card("Diamonds", "Queen"),Card("Diamonds", "Jack"),Card("Diamonds", "10")])
    
    def give_card(self, card: Card) -> None:
        self._cards.append(card)

    @abstractmethod
    def make_move(self, table) -> str:
        pass
