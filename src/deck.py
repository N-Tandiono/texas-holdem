from card import Card
import random

class Deck:
    def __init__(self):
        self.cards_in_deck = []
        self.CreateDeck()

    def CreateDeck(self):
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for suit in suits:
            for val in vals:
                self.cards_in_deck.append(Card(suit, val))

        random.shuffle(self.cards_in_deck)

    def PrintDeck(self):
        for card in self.cards_in_deck:
            print(card)
    