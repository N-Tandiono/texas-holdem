from player.player import Player
from table import Table

class HumanPlayer(Player):

    def make_move(self, table: Table) -> str:
        print(self._name + "'s Turn")

        # Print Table Cards
        print("Table:    [ ", end="")
        for i in range(len(table._table_cards) - 1):
            print(table._table_cards[i] , end=" | ")
        if len(table._table_cards) == 0:
            print(" ]")
        else:
            print(str(table._table_cards[len(table._table_cards) - 1]) + " ]")

        # Your Cards
        print("Cards:    [ " + str(self._cards[0]) + " | " + str(self._cards[1]) + "]")

        # Chips Owned
        print("Chips:    [ ", end="")
        for i in range(len(table._players) - 1):
            print("(" + str(i + 1) + ") " + str(table._players[i]._role) + " " + str(table._players[i]._chips) , end=" | ")
        print("(" + str(len(table._players)) + ") " + str(table._players[len(table._players) - 1]._role) + " " + str(table._players[len(table._players) - 1]._chips) + " ]")
        
        # Chips In Play
        print("In Play:  [ ", end="")
        for i in range(len(table._players) - 1):
            print("(" + str(i + 1) + ") " + str(table._players[i]._role) + " " +str(table._players[i]._round_bet) , end=" | ")
        print("(" + str(len(table._players)) + ") " + str(table._players[len(table._players) - 1]._role) + " " +str(table._players[len(table._players) - 1]._round_bet) + " ]")

        print("Pot is currently at: " + str(table.pot))
        print("You have " + str(self._chips) + " chips")
        
        # For Testing:
        print("Highest Combination: " + self._highest_combination)

        action = input("What do you want to do? ").split(' ')
        move = action[0]
        
        if move == "raise":
            self.move_raise(action[1], table)

        elif move == "check" or move == "call":
            self.move_call(table)

        elif move == "fold":
            self.move_fold()

        elif move == "all-in":
            self.move_all_in(table)
            
        else:
            raise Exception

        return move