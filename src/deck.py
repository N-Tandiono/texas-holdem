from card import Card
import random

class Deck:
    def __init__(self):
        self.cards_in_deck = []
        self.create_deck()

    def create_deck(self) -> None:
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        for suit in suits:
            for val in vals:
                self.cards_in_deck.append(Card(suit, val))

        random.shuffle(self.cards_in_deck)

    def print_deck(self) -> None:
        for card in self.cards_in_deck:
            print(card)
    
    def remove_top(self) -> None:
        return self.cards_in_deck.pop()