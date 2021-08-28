from player.player import Player

class HumanPlayer(Player):

    def make_move(self) -> str:
        move = str(input("What do you want to do? "))
        return move