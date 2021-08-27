from player import Player

class Players:
    def __init__(self, num_players):
        self.players = []
        self.PopulateTable(num_players)

    def PopulateTable(self, num_players):
        for _ in range(num_players):
            self.players.append(Player())