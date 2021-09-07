from card import Card
from player.player import Player

class Table():

    _players = []
    _table_cards = [] * 5
    pot = 0
    round = 0

    def attach(self, observer: Player) -> None:
        self._players.append(observer)

    def detach(self, observer: Player) -> None:
        self._players.remove(observer)

    def notify(self) -> None:
        for observer in self._players:
            observer.update(self)

    def add_table_cards(self, new_card: Card) -> None:
        self._table_cards.append(new_card)
        self.notify()

    def table_same_bet(self, prev: int) -> bool:
        # pre-condition, there is always at least one player at the table to play (assumption)
        bet = self._players[0]._round_bet # Take bet of the first person to compare with

        for player in self._players:
            if player._round_bet != bet:
                return False

        if bet == prev:
            return False

        return True