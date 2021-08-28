from player.player import Player

class Table():

    _players = []
    _table_cards = []

    def attach(self, observer: Player) -> None:
        self._players.append(observer)

    def detach(self, observer: Player) -> None:
        self._players.remove(observer)

    def notify(self) -> None:
        for observer in self._players:
            observer.update(self)


