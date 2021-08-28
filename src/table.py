from player.player import Player

class Table():

    _observers = []
    _table_cards = []

    def attach(self, observer: Player) -> None:
        self._observers.append(observer)

    def detach(self, observer: Player) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
            print(observer.make_move())

