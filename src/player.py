class Player:
    def __init__(self):
        self.cards = []
        self.money = 50 # Temporary set
    
    def __repr__(self):
        return repr(self.cards)

    def GiveCard(self, card):
        self.cards.append(card)