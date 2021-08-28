from abc import ABC, abstractmethod

from card import Card

class Player(ABC):

    def __init__(self):
        self._cards = []
        self._history = []
        self._round_bet = None
        self._chips = 0
        self._is_valid_player = True
        self._highest_combination = str

    def update(self, table) -> None:
        for card in table._table_cards:
            if card not in self._cards:
                self._cards.append(card)
    
    def give_card(self, card: Card) -> None:
        self._cards.append(card)

    @abstractmethod
    def make_move(self) -> str:
        pass