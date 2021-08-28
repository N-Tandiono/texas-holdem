from deck import Deck
from player.bot import Bot
from player.human_player import HumanPlayer
from player.player import Player
from table import Table

class Game():
    def __init__(self):
        self._deck = Deck()
        self._table = Table()

    def template_play_game(self):
        
        # Game continues until there is one player left at the table
        while len(self._table._players) > 1:
            self.template_play_round()


    def template_play_round(self) -> None:
        
        # Create players which will be playing on table
        self.generate_players()
        
        # Give all players in the table their first card
        self.give_players_card()
        
        # Give all players in the table their second card
        self.give_players_card()
        
        # Place three cards on table for preflop
        self.generate_pre_flop()

        # Request user actions
        self.generate_actions()

        # Place card on table for turn
        self.generate_turn()
        
        # Request user actions
        self.request_actions()
        
        # Place card on table for river
        self.generate_river()

        # Request user actions
        self.request_actions()

if __name__ == "__main__":
    table = Table()
    table.attach(HumanPlayer())
    table.notify()