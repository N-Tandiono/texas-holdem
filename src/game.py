from deck import Deck
from player.bot import Bot
from player.human_player import HumanPlayer
from player.player import Player
from table import Table

class Game():
    def __init__(self):
        self._deck = Deck()
        self._table = Table()
        self._big_blind = 1 # Since there are always 2 players, second closest player left (index 1 in players table starts) 
        self._small_blind = 0 # Since there are always 2 players, closest player left (index 0 in players table starts) 

    def template_play_game(self) -> None:

        # Create players which will be playing on table
        self.generate_players()

        # Game continues until there is one player left at the table
        # while len(self._table._players) > 1:
        self.template_play_round()


    def template_play_round(self) -> None:
                
        # Give all players in the table their first card
        self.give_players_card()
        
        # Give all players in the table their second card
        self.give_players_card()
        
        # Place three cards on table for preflop
        self.generate_pre_flop()

        # Request user actions
        self.request_actions()

        # Place card on table for turn
        self.generate_turn()
        
        # Request user actions
        self.request_actions()
        
        # Place card on table for river
        self.generate_river()

        # Request user actions
        self.request_actions()

    def generate_players(self) -> None:
        for _ in range(2): # TODO: Temporarily set as 2 human players
            self._table.attach(HumanPlayer())

    def give_players_card(self) -> None:
        for player in self._table._players:
            player.give_card(self._deck.remove_top())

    def generate_pre_flop(self) -> None:
        for _ in range(3):
            self._table.add_table_cards(self._deck.remove_top())

    def generate_turn(self) -> None:
        self._table.add_table_cards(self._deck.remove_top())
    
    def generate_river(self) -> None:
        self._table.add_table_cards(self._deck.remove_top())

    def request_actions(self) -> None:
        # Response of player.make_move() can either be raise or check or call or fold or all-in
        # When everyone checks in a rotation,
        while not self._table.table_same_bet():
            i = 0
            if self._table._players[i]._is_valid_player: # If valid player, player can play in pot
                action = self._table._players[i].make_move()
                if action == "raise":
                    # On raise, players continue until check or all-in 
                    print("Raised")
                    pass
                elif action == "check":
                    # On Check, player does not choose to raise and no chips are taken
                    print("Checked")
                    pass
                elif action == "call":
                    # On Call, player matches previous bet 
                    print("Called")
                    pass
                elif action == "fold":
                    # Player should be invalid from table and not eligible of winning
                    # Does not spend any more chips on that round
                    print("Folded")
                    pass
                elif action == "all-in":
                    # Player goes all in, distribution of pot should be considered
                    # If a player cannot match a raise value, they should be all-in / fold
                    # If they already all-in the previous round, they skip turn
                    print("All-in")
                    pass
                else:
                    raise Exception
            i += 1

            if i >= len(self._table._players):
                i = 0

if __name__ == "__main__":
    game = Game()
    game.template_play_game()