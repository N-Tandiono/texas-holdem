from player.player import Player
from table import Table

class HumanPlayer(Player):

    def make_move(self, table: Table, status: str) -> str:
        print(self._name + " turn")
        if status == "big":
            print("You are Big Blind")
            table.pot += 50
            self._round_bet += 50
            self._chips -= 50

        if status == "small":
            print("You are Small Blind")
            table.pot += 25
            self._round_bet += 25
            self._chips -= 25

        print("Pot is currently at: " + str(table.pot))
        print("This action, player has contributed " + str(self._round_bet))
        print("You have " + str(self._chips) + " chips")
        action = input("What do you want to do? ").split(' ')
        move = action[0]
        
        if move == "raise":
            print("RAISING BY: " + action[1])

            table.pot += int(action[1])
            self._round_bet += int(action[1])
            self._chips -= int(action[1])

            print("Raised")

        elif move == "check" or move == "call":
            contribution = 0
            for player in table._players:
                contribution = max(contribution, player._round_bet - self._round_bet)
            table.pot += contribution
            self._round_bet += contribution
            self._chips -= contribution
            print(str(contribution) + "to match for call")
        elif move == "fold":
            self._is_valid_player = False
            print("Folded")

        elif move == "all-in":
            print("All-in")
            table.pot += self._chips
            self._round_bet += self._chips
            self._chips -= self._chips
        else:
            raise Exception

        return move