from player.player import Player
from table import Table

class HumanPlayer(Player):

    def make_move(self, table: Table) -> str:
        print(self._name + " turn")

        # Print Table Cards
        print("Table:    [ ", end="")
        for i in range(len(table._table_cards) - 1):
            print(table._table_cards[i] , end=" | ")
        print(str(table._table_cards[len(table._table_cards) - 1]) + " ]")

        # Your Cards
        print("Cards:    [ " + str(self._cards[0]) + " | " + str(self._cards[1]) + "]")

        # Chips
        print("Chips:    [ ", end="")
        for i in range(len(table._players) - 1):
            print("(" + str(i + 1) + ") " + str(table._players[i]._role) + " " + str(table._players[i]._chips) , end=" | ")
        print("(" + str(len(table._players)) + ") " + str(table._players[len(table._players) - 1]._role) + " " + str(table._players[len(table._players) - 1]._chips) + " ]")
        
        # Chips
        print("In Play:  [ ", end="")
        for i in range(len(table._players) - 1):
            print("(" + str(i + 1) + ") " + str(table._players[i]._round_bet) , end=" | ")
        print("(" + str(len(table._players)) + ") " + str(table._players[len(table._players) - 1]._round_bet) + " ]")

        print("Pot is currently at: " + str(table.pot))
        print("You have " + str(self._chips) + " chips")
        
        # For Testing:
        print("Highest Combination: " + self._highest_combination)
        
        action = input("What do you want to do? ").split(' ')
        move = action[0]
        
        if move == "raise":
            print("RAISING BY: " + action[1])
            contribution = 0
            for player in table._players:
                contribution = max(contribution, player._round_bet - self._round_bet)
            table.pot += contribution + int(action[1])
            self._round_bet += contribution + int(action[1])
            self._chips -= contribution + int(action[1])

        elif move == "check" or move == "call":
            contribution = 0
            for player in table._players:
                contribution = max(contribution, player._round_bet - self._round_bet)
            table.pot += contribution
            self._round_bet += contribution
            self._chips -= contribution
            print(str(contribution) + " to match for call")
        elif move == "fold":
            self._is_valid_player = False

        elif move == "all-in":
            table.pot += self._chips
            self._round_bet += self._chips
            self._chips -= self._chips
        else:
            raise Exception

        return move