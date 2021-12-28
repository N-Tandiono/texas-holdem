from abc import ABC, abstractmethod

from card import Card
from compare import find_highest_combination

from logger import Logger

class Player(ABC):

    def __init__(self, name: str, starting_chips: int):
        self._name = name
        self._cards = []
        self._round_bet = 0
        self._chips = starting_chips
        self._role = ""
        self._is_valid_player = True
        value, combination = find_highest_combination(self._cards)

        self._highest_combination = combination
        self.value = value

    def update(self, table) -> None:
        # Called on addition of a card to the table.
        # Recalculate odds and highest_combination
        value, combination = find_highest_combination(self._cards + table._table_cards)
        
        self._highest_combination = combination
        self.value = value

    def give_card(self, card: Card) -> None:
        self._cards.append(card)
        value, combination = find_highest_combination(self._cards)

        self._highest_combination = combination
        self.value = value

    def move_raise(self, amount, table):
        print("Raising by: " + amount)
        contribution = 0
        for player in table._players:
            contribution = max(contribution, player._round_bet - self._round_bet)

        # Check if player can afford to pay up contribution + int(amount)
        # Cannot raise over the number of chips player has
        table.pot += min(contribution + int(amount), self._chips)
        self._round_bet += min(contribution + int(amount), self._chips)
        self._chips -= min(contribution + int(amount), self._chips)
        
        
    def move_call(self, table):
        contribution = 0

        for player in table._players:
            contribution = max(contribution, player._round_bet - self._round_bet)

        # Check if player can afford to pay up contribution
        if self._chips >= contribution:
            table.pot += contribution
            self._round_bet += contribution
            self._chips -= contribution
            print(str(contribution) + " to match for call")
        else:
            # If no, prompt all-in
            self.move_all_in(table)
        

    def move_fold(self):
        self._is_valid_player = False
    
    def move_all_in(self, table):
        table.pot += self._chips
        self._round_bet += self._chips
        self._chips -= self._chips

    @abstractmethod
    def make_move(self, table) -> str:
        pass
