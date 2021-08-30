from abc import ABC, abstractmethod

from card import Card

class Player(ABC):

    def __init__(self, name: str):
        self._name = name
        self._cards = []
        self._round_bet = 0
        self._chips = 500
        self._role = ""
        self._is_valid_player = True
        self._highest_combination = str

    def update(self, table) -> None:
        # Recalculate odds and highest_combination
        pass
    
    def give_card(self, card: Card) -> None:
        self._cards.append(card)

    @abstractmethod
    def make_move(self, table) -> str:
        pass
