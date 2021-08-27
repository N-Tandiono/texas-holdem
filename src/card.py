class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return 'Card with value of ' + self.value + ' and suit of ' + self.suit