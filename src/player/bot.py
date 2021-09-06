from player.player import Player
from strategy.bluff_strategy import BluffStrategy
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
        # Goal: Will improve over time 
        
        # Danger cards
        # Winning cards

        decided_strategy = BluffStrategy()

        # Assign Strategy
        # Bluff / Slow Play / Push for Chips
        self._strategy = decided_strategy

        # Based on strategy, make move
        move = self.strategy.generate_move(table)

        # Below is repetition from Human Player, will need refactoring
        if move == "raise":
            self.move_raise(100, table)

        elif move == "check" or move == "call":
            self.move_call(table)

        elif move == "fold":
            self.move_fold()

        elif move == "all-in":
            self.move_all_in(table)
            
        else:
            raise Exception

        return move
        

    @property
    def strategy(self) -> Strategy:
        return self._strategy
