from player.player import Player
from table import Table

class Bot(Player):

    def make_move(self, table: Table) -> str:
        return "Check"