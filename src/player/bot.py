from player.player import Player
from table import Table

class Bot(Player):

    def make_move(self, table: Table) -> str:
        print(self._name + " turn")
        
        contribution = 0
        for player in table._players:
            contribution = max(contribution, player._round_bet - self._round_bet)
        table.pot += contribution
        self._round_bet += contribution
        self._chips -= contribution
        print(str(contribution) + " to match for call")

        return "check"