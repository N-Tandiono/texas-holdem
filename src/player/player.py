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
        # self._highest_combination = find_highest_combination([Card("Diamonds", "9"),Card("Hearts", "4"),Card("Clubs", "5"),Card("Clubs", "Ace"),Card("Clubs", "2"),Card("Diamonds", "2"),Card("Diamonds", "3")])
        # print(self._highest_combination)
        
    def give_card(self, card: Card) -> None:
        self._cards.append(card)

    def move_raise(self, amount, table):
        print("RAISING BY: " + amount)
        contribution = 0
        for player in table._players:
            contribution = max(contribution, player._round_bet - self._round_bet)

        # Check if player can afford to pay up contribution + int(amount)

        table.pot += contribution + int(amount)
        self._round_bet += contribution + int(amount)
        self._chips -= contribution + int(amount)

        # If no, prompt all-in
    
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
