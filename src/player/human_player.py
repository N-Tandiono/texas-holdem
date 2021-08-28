from player.player import Player

class HumanPlayer(Player):

    def make_move(self) -> str:
        return "raise"