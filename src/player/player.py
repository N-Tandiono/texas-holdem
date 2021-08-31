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
        self._highest_combination = ""

    def update(self, table) -> None:
        # Called on addition of a card to the table.
        
        # self._highest_combination = find_highest_combination(self._cards + table._table_cards)
        # Recalculate odds and highest_combination

        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        vals = ['10', 'Jack', 'Queen', 'King', 'Ace']

        find_highest_combination([Card("Diamonds", "10"),Card("Spades", "10"),Card("Hearts", "10"),Card("Clubs", "11"),Card("Diamonds", "Ace")])


        pass
    
    def give_card(self, card: Card) -> None:
        self._cards.append(card)

    @abstractmethod
    def make_move(self, table) -> str:
        pass
