from player.player import Player
from strategy.bluff import BluffStrategy
from strategy.strategy import Strategy
from table import Table

class Bot(Player):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._confidence = 100
        self._strategy = BluffStrategy()

    def make_move(self, table: Table) -> str:
        print(self._name + " turn")

        # Look at bot cards

        # Look at table cards

        # Does it like it, confidence level

        # How many chips does it have

        # Think of a strategy
        # Strategy based on confidence level and perspective
        # Will improve over time

        # Danger cards
        # Winning cards

        # Bluff / Slow Play / Push for Chips

        # Based on strategy, make move
        contribution = 0
        for player in table._players:
            contribution = max(contribution, player._round_bet - self._round_bet)
        table.pot += contribution
        self._round_bet += contribution
        self._chips -= contribution
        print(str(contribution) + " to match for call")

        return self.strategy.generate_move(table)

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy