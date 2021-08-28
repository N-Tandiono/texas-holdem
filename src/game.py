from player.bot import Bot
from player.human_player import HumanPlayer
from player.player import Player
from table import Table

if __name__ == "__main__":
    table = Table()
    table.attach(HumanPlayer())
    table.notify()