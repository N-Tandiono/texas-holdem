from card import Card
from compare import convert_from_score, is_card_in, score_combination, resolve_draw
from deck import Deck
from player.bot import Bot
from player.human_player import HumanPlayer
from player.player import Player
from table import Table

# Import constants
from constants import rank, action

class Game():
    def __init__(self):
        self._deck = Deck()
        self._table = Table()
        self.lead = None
        self._big_blind = 1 # Since there are always 2 players, second closest player left (index 1 in players table starts) 
        self._small_blind = 0 # Since there are always 2 players, closest player left (index 0 in players table starts) 

    def template_play_game(self) -> None:

        # Create players which will be playing on table
        self.generate_players()

        # Game continues until there is one player left at the table
        while len(self._table._players) > 1:
            self.template_play_round()

        print(self._table._players[0]._name + " was the last person on the table.")

    def template_play_round(self) -> None:
        
        print("=== START ROUND ===")
        # Give all players in the table their first card
        self.give_players_card()
        
        # Give all players in the table their second card
        self.give_players_card()
        
        print("FIRST ACTION")
        # Request user actions
        self.request_actions()

        # Place three cards on table for flop
        self.generate_flop()

        print("SECOND ACTION")
        # Request user actions
        self.request_actions()

        # Place card on table for turn
        self.generate_turn()
        
        print("THIRD ACTION")
        # Request user actions
        self.request_actions()
        
        # Place card on table for river
        self.generate_river()

        print("FOURTH ACTION")
        # Request user actions
        self.request_actions()
        
        # Check if round is finished and reveal (Folded Players)
        self.reveal()

        self.reset_round()
        print("=== END ROUND ===")

    def generate_players(self) -> None:
        self._table.attach(HumanPlayer("Player 1", 1000))
        self._table.attach(HumanPlayer("Player 2", 500))
        

    def give_players_card(self) -> None:
        for player in self._table._players:
            player.give_card(self._deck.remove_top())

    def generate_flop(self) -> None:
        for _ in range(3):
            self._table.add_table_cards(self._deck.remove_top())

    def generate_turn(self) -> None:
        self._table.add_table_cards(self._deck.remove_top())
    
    def generate_river(self) -> None:
        self._table.add_table_cards(self._deck.remove_top())

    def request_actions(self) -> None:
        # Response of player.make_move() can either be raise or check or call or fold or all-in
        # When everyone checks in a rotation,

        # Get starting player
        i = self._big_blind + 1
        if i >= len(self._table._players):
            i = 0

        if self._table.round == 0:
            # Big blind and small blind contributions
            self._table.pot += 50
            self._table._players[self._big_blind]._round_bet += 50
            self._table._players[self._big_blind]._chips -= 50

            self._table.pot += 25
            self._table._players[self._small_blind]._round_bet += 25
            self._table._players[self._small_blind]._chips -= 25

            # Assign roles to new players
            self._table._players[self._big_blind]._role = "BB"
            self._table._players[self._small_blind]._role = "SB"

        self.lead = i - 1
        if self.lead < 0:
            self.lead = len(self._table._players) - 1

        while True:
            
            print("================================")
            
            if self._table._players[i]._is_valid_player and self._table._players[i]._chips == 0:
                print("Player is all-in")

            elif not self._table._players[i]._is_valid_player:
                print("Player has folded")

            elif self._table._players[i]._is_valid_player and self._table._players[i]._chips > 0: # If valid player, player can play in pot
                
                # Check if they are the only one not folded
                number_not_folded = 0
                for player in self._table._players:
                    if player._is_valid_player:
                        number_not_folded += 1

                if number_not_folded == 1:
                    print("All Players have folded except one")
                    break
                
                player_move = self._table._players[i].make_move(self._table)

                if player_move in action.RAISE:
                    # On raise, players continue until check or all-in 
                    print("Raised")
                    self.lead = i - 1
                    if self.lead < 0:
                        self.lead = len(self._table._players) - 1
                    pass
                elif player_move in action.CHECK:
                    # On Check, player does not choose to raise and no chips are taken
                    print("Checked")
                    pass
                elif player_move in action.CALL:
                    # On Call, player matches previous bet 
                    print("Called")
                    pass
                elif player_move in action.FOLD:
                    # Player should be invalid from table and not eligible of winning
                    # Does not spend any more chips on that round
                    print("Folded")
                    # Check other players, if there is only 1 left that hasn't folded, they win and round ends
                    pass
                elif player_move in action.ALL_IN :
                    # Player goes all in, distribution of pot should be considered
                    # If a player cannot match a raise value, they should be all-in / fold
                    # If they already all-in the previous round, they skip turn
                    print("All-in")
                    pass
                else:
                    raise Exception
            
            if not self._table._players[i]._is_valid_player:
                print("Player has folded")
                # Check if all players are all-in, if yes, reveal

                number_not_folded = 0
                for player in self._table._players:
                    if player._is_valid_player:
                        number_not_folded += 1

                if number_not_folded == 1:
                    print("All Players have folded except one")
                    break
                elif number_not_folded == 0:
                    raise Exception("All players are folded: this should not be possible")

            if self._table._players[i]._is_valid_player and self._table._players[i]._chips == 0:
                print("Player is all-in")
                # Check if all players are all-in, if yes, reveal

                continue_play = False
                for player in self._table._players:
                    if player._is_valid_player and player._chips > 0:
                        continue_play = True

                if not continue_play:
                    print("All Players are all-in")
                    break
            
            if i == self.lead:
                # Leave and reset
                break

            i += 1
            if i >=  len(self._table._players):
                i = 0

        # Increment table round for no extra pay from BB or SB
        self._table.round += 1

        print("================================")

    def reset_roles(self) -> None:
        for player in self._table._players:
            player._role = ""
    
    def reveal(self):
        # Firstly get the highest combination
        # If there is a draw, check value representation
        player_highest_comb = []

        # Resolving Draws
        # Royal Flush - Can't draw this
        # Straight Flush - Highest range
        # Four of a Kind - Highest Four of a Kind or Kicker determines
        # Full House - Highest 3, then highest 2
        # Flush - Highest Cards of Flush
        # Straight - Highest range
        # Three of a Kind - Highest 3
        # Two Pair - Highest Pair, Second Pair or Kicker determines
        # Pair - Highest Pair, Kickers determines
        # Highest Card in order

        # Sort distribution of pot
        # Sort all-ins, if winner but does not get entire pot

        # Second highest winner
        # What if second highest is also all-in who does not get entire pot

        results = {}
        for player in self._table._players:
            if player._is_valid_player:
                if score_combination(player._highest_combination) not in results:
                    results[score_combination(player._highest_combination)] = []
                results[score_combination(player._highest_combination)].append(player)

        for i in range(1, 11):
            if i in results:
                player_highest_comb = results[i]

                # Resolve Draws Here
                player_highest_comb = resolve_draw(player_highest_comb, player_highest_comb[0]._highest_combination)

            for player in player_highest_comb:
                player._chips += player._round_bet
                self._table.pot -= player._round_bet

                for table_player in self._table._players:
                    if table_player not in player_highest_comb:
                        player._chips += min(player._round_bet, table_player._round_bet // len(player_highest_comb))
                        self._table.pot -= min(player._round_bet, table_player._round_bet // len(player_highest_comb))
                        table_player._round_bet -= min(player._round_bet, table_player._round_bet // len(player_highest_comb))

                player._round_bet = 0

            if self._table.pot == 0:
                print("Pot now Empty")
                break
                        
        # Give money for reward winning
        # From pot, give to winner, divided amongst everyone
        # TODO: Fix up and find out a more accurate measurement especially for all-ins
        

        # Chips Owned
        print("Chips:    [ ", end="")
        for k in range(len(self._table._players) - 1):
            print("(" + str(k + 1) + ") " + str(self._table._players[k]._role) + " " + str(self._table._players[k]._chips) , end=" | ")
        print("(" + str(len(self._table._players)) + ") " + str(self._table._players[len(self._table._players) - 1]._role) + " " + str(self._table._players[len(self._table._players) - 1]._chips) + " ]")

        # Chips In Play
        print("In Play:  [ ", end="")
        for j in range(len(self._table._players) - 1):
            print("(" + str(j + 1) + ") " + str(self._table._players[j]._role) + " " +str(self._table._players[j]._round_bet) , end=" | ")
        print("(" + str(len(self._table._players)) + ") " + str(self._table._players[len(self._table._players) - 1]._role) + " " +str(self._table._players[len(self._table._players) - 1]._round_bet) + " ]")

        print("Winners:    [ ", end="")
        for i in range(len(player_highest_comb) - 1):
            print(str(player_highest_comb[i]._name) , end=", ")
        print(str(player_highest_comb[len(player_highest_comb) - 1]._name) + " ]")
        print("Combination: " + str(player_highest_comb[len(player_highest_comb) - 1]._highest_combination))

        # print(self._table._table_cards)
        # print(self._table._players[0]._cards)
        # print(self._table._players[1]._cards)

        # If player all-ins and loses, they should be dettached from table as they are no longer playing
        to_remove = []
        for player in self._table._players:
            if player._chips <= 0:
                to_remove.append(player)
        for player in to_remove:
            print("Removing " + player._name + " from table.")
            self._table.detach(player)
        
        # Reset Round
        results = {}

    def reset_round(self):
        for player in self._table._players:
            player._cards = []
            player._round_bet = 0
            player._is_valid_player = True
            player._highest_combination = "High Card"

        self._deck = Deck()
        self._table._table_cards = [] * 5
        self._table.pot = 0
        self._table.round = 0
        self.reset_roles()

        # TODO: Clean up to functions
        self._big_blind += 1
        if self._big_blind >= len(self._table._players):
            self._big_blind = 0
        while not self._table._players[self._big_blind]._is_valid_player:
            self._big_blind += 1
            if self._big_blind >= len(self._table._players):
                self._big_blind = 0

        self._small_blind += 1
        if self._small_blind >= len(self._table._players):
            self._small_blind = 0
        while not self._table._players[self._small_blind]._is_valid_player:
            self._small_blind += 1
            if self._small_blind >= len(self._table._players):
                self._small_blind = 0

if __name__ == "__main__":
    game = Game()
    game.template_play_game()