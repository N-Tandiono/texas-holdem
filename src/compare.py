from itertools import permutations
from card import Card

def find_highest_combination(cards) -> str:
    # Card Rankings:
    # 1. Royal Flush
    # 2. Straight Flush
    # 3. Four of a Kind
    # 4. Full House
    # 5. Flush
    # 6. Straight
    # 7. Three of a Kind
    # 8. Two Pair
    # 9. Pair
    # 10. High Card

    if has_royal_flush(cards):
        return "Royal Flush"
    elif has_straight_flush(cards):
        return "Straight Flush"
    elif has_four_kind(cards):
        return "Four of a Kind"
    elif has_full_house(cards):
        return "Full House"
    elif has_flush(cards):
        return "Flush"
    elif has_straight(cards):
        return "Straight"
    elif has_three_kind(cards):
        return "Three of a Kind"
    elif has_two_pair(cards):
        return "Two Pair"
    elif has_pair(cards):
        return "Pair"
    else:
        return "High Card"

def has_royal_flush(cards):
    # Royal Flush have 10, J, Q, K, A
    # Same suit
    possibilities = []

    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    vals = ['10', 'Jack', 'Queen', 'King', 'Ace']

    for suit in suits:
        hand = []
        for val in vals:
            hand.append(Card(suit, val))
        possibilities.append(hand)

    for pos in possibilities:
        valid = True
        for needed_card in pos:
            if not is_card_in(needed_card, cards):
                valid = False
        if valid == True:
            return True
    return False

def has_straight_flush(cards):
    pass

def has_four_kind(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    if 4 in hash.values():
        return True
    return False

def has_full_house(cards):
    pass

def has_flush(cards):
    pass

def has_straight(cards):
    pass

def has_three_kind(cards):
    pass

def has_two_pair(cards):
    pass

def has_pair(cards):
    pass

def is_equal(card1, card2):
    if card1.suit == card2.suit and card1.value == card2.value:
        return True
    return False

def is_card_in(card, array):
    for c in array:
        if is_equal(card, c):
            return True
    return False