from player.player import Player
from strategy.bluff_strategy import BluffStrategy
from strategy.push_strategy import PushStrategy
from strategy.fold_strategy import FoldStrategy
from strategy.strategy import Strategy
from table import Table

from logger import Logger
import random

class Bot(Player):

    def __init__(self, name: str, starting_chips: int) -> None:
        super().__init__(name, starting_chips)
        # Similar concept to counterfactual regret minimization, adding regret
        # Bot with higher regret has a higher chance to all-in on seemingly good hands and past history
        # High level classified regret or chip raise, will use past hands
        # Pre-flop - personal winrate percentage with knowledge on pair potential / flush and straight
        # On Flop - see percent, chances of winning and regret rate to judge rest
        # Turn - Does card help or not, how committed was the bot previously? Percent of it winning, position location
        # River - Final move -> Should it check first and then raise, etc.
        self._regret = 0
        self._strategy = None

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

        decided_strategy = self.getStrategy(table)

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
            self.move_fold(table)

        elif move == "all-in":
            self.move_all_in(table)
            
        else:
            raise Exception

        return move

    def getStrategy(self, table):
        table._logger.write(f"[Bot] {self._name} planning strategy")
        table._logger.write(f"[Bot] {self._name} has regret {self._regret}")
        
        # Which round are we in
        # Security in hand

        # Get move history of players we are versing

        # Moves history, has one been played before with this

        # Bot with higher regret has a higher chance to all-in on seemingly good hands and past history
        # High level classified regret or chip raise, will use past hands
        # Pre-flop - personal winrate percentage with knowledge on pair potential / flush and straight
        # On Flop - see percent, chances of winning and regret rate to judge rest
        # Turn - Does card help or not, how committed was the bot previously? Percent of it winning, position location
        # River - Final move -> Should it check first and then raise, etc.

        wr_chance = 40 # Calculate

        wr_chance_adjusted = random.randint(wr_chance - 10, wr_chance + 10)
        regret_chance_adjusted = random.randint(self._regret - 10, self._regret + 10)

        if wr_chance_adjusted + regret_chance_adjusted > 100: # High chance
            return PushStrategy()
        elif wr_chance_adjusted + regret_chance_adjusted < 10: # Will lose definitely, but chips are safe level
            # Need to consider safe chip level
            return FoldStrategy()
        elif wr_chance_adjusted + regret_chance_adjusted < 20: # Calculated bluff
            return BluffStrategy()
        

    @property
    def strategy(self) -> Strategy:
        return self._strategy
