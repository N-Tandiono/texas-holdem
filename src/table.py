from deck import Deck
from players import Players

class Table:
    def __init__(self):
        self.table_deck = Deck()
        self.table_players = Players(2)
        self.table_cards = []

    def PlayRound(self):
        # Deal First Card To Players
        for player in self.table_players.players:
            player.GiveCard(self.DrawCard())

        # Deal Second Card To Players
        for player in self.table_players.players:
            player.GiveCard(self.DrawCard())

        # Play Actions

        # Pre-Flop
        # Deal 3 cards and show on table
        for _ in range(3):
            self.table_cards.append(self.DrawCard())

        # Play Actions

        # Turn
        # Deal 1 card and show on table
        self.table_cards.append(self.DrawCard())

        # Play Actions

        # River
        # Deal 1 card and show on table
        self.table_cards.append(self.DrawCard())

        # Play Actions

        # Reveal

        # Print Cards Everyone Has
        for player in self.table_players.players:
            print(player)
        print(self.table_cards)

    def DrawCard(self):
        return self.table_deck.RemoveTop()