from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self):
        self._cards = []
        self._chips = 0
        self._highest_combination = str

    def update(self, table) -> None:
        self._cards.append(table._table_cards)
        for card in table._table_cards:
            if card not in self._cards:
                self._cards.add(card)
       
    @abstractmethod
    def make_move(self) -> str:
        pass