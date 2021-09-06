from itertools import permutations
from card import Card
from constants import rank

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

def score_combination(type: str) -> int:
    if type == "Royal Flush":
        return rank.ROYAL_FLUSH
    if type == "Straight Flush":
        return rank.STRAIGHT_FLUSH
    if type == "Four of a Kind":
        return rank.FOUR_OF_A_KIND
    if type == "Full House":
        return rank.FULL_HOUSE
    if type == "Flush":
        return rank.FLUSH
    if type == "Straight":
        return rank.STRAIGHT
    if type == "Three of a Kind":
        return rank.THREE_OF_A_KIND
    if type == "Two Pair":
        return rank.TWO_PAIR
    if type == "Pair":
        return rank.PAIR
    else:
        return 10

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
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    for card in cards:
        valid = True
        for i in range(1, 5):
            if card.value == "Ace":
                needed_card = str(int(0) + i)
            elif card.value in ["Jack", "Queen", "King"]:
                needed_card = ""
            else:
                needed_card = str(int(card.value) + i)

            if needed_card == "1":
                needed_card = "Ace"
            if needed_card == "11":
                needed_card = "Jack"
            elif needed_card == "12":
                needed_card = "Queen"
            elif needed_card == "13":
                needed_card = "King"
            elif needed_card == "14":
                needed_card = "Ace"
            if not is_card_in(Card(card.suit, needed_card), cards) or needed_card not in hash:
                valid = False
        if valid:
            return True
    return False

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
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    if 3 in hash.values() and 2 in hash.values():
        return True
    return False

def has_flush(cards):
    hash = {}
    for card in cards:
        if card.suit in hash:
            hash[card.suit] += 1
        else:
            hash[card.suit] = 1

    if 5 in hash.values():
        return True
    return False

def has_straight(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    for card in cards:
        valid = True
        for i in range(1, 5):
            if card.value == "Ace":
                needed_card = str(int(0) + i)
            elif card.value in ["Jack", "Queen", "King"]:
                needed_card = ""
            else:
                needed_card = str(int(card.value) + i)

            if needed_card == "1":
                needed_card = "Ace"
            if needed_card == "11":
                needed_card = "Jack"
            elif needed_card == "12":
                needed_card = "Queen"
            elif needed_card == "13":
                needed_card = "King"
            elif needed_card == "14":
                needed_card = "Ace"
            if needed_card not in hash:
                valid = False
        if valid:
            return True
    return False

def has_three_kind(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    if 3 in hash.values():
        return True
    return False

def has_two_pair(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    values = list(hash.values())
    pairs = 0
    for val in values:
        if val == 2:
            pairs += 1

    # If pairs >= 2, take best 2 pairs.
    # TODO: Get top two pairs
    if pairs >= 2:
        return True
    return False

def has_pair(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    if 2 in hash.values():
        return True
    return False

def is_equal(card1, card2):
    if card1.suit == card2.suit and card1.value == card2.value:
        return True
    return False

def is_card_in(card, array):
    for c in array:
        if is_equal(card, c):
            return True
    return False