from itertools import permutations
from card import Card
from constants import rank

# TODO: Fix case
# [Info] Table has [8 Of Hearts, 8 Of Diamonds, 7 Of Hearts, 4 Of Hearts, Jack Of Hearts]
# [Info] Player 1 has [9 Of Spades, 3 Of Clubs]
# [Info] Player 2 has [5 Of Clubs, Queen Of Diamonds]

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
        return value_royal_flush(cards), "Royal Flush"
    elif has_straight_flush(cards):
        return value_straight_flush(cards), "Straight Flush"
    elif has_four_kind(cards):
        return value_four_kind(cards), "Four of a Kind"
    elif has_full_house(cards):
        return value_full_house(cards), "Full House"
    elif has_flush(cards):
        return value_flush(cards), "Flush"
    elif has_straight(cards):
        return value_straight(cards), "Straight"
    elif has_three_kind(cards):
        return value_three_kind(cards), "Three of a Kind"
    elif has_two_pair(cards):
        return value_two_pair(cards), "Two Pair"
    elif has_pair(cards):
        return value_pair(cards), "Pair"
    else:
        return value_high_card(cards, []), "High Card"

def resolve_draw(players, type):

    scores = {}
    for player in players:
        first = player.value.split(" ")[0]
        if first in scores:
            scores[first].append(player)
        else:
            scores[first] = [player]

    if type == "Royal Flush":
        return players
    if type == "Straight Flush":
        return get_highest_score(scores, True)
    if type == "Four of a Kind":
        return get_highest_score(scores, False)
    if type == "Full House":
        return get_highest_score(scores, False)
    if type == "Flush":
        return get_highest_score(scores, False)
    if type == "Straight":
        return get_highest_score(scores, True)
    if type == "Three of a Kind":
        return get_highest_score(scores, False)
    if type == "Two Pair":
        return get_highest_score(scores, False)
    if type == "Pair":
        return get_highest_score(scores, False)
    else:
        return get_highest_score(scores, False)

def get_highest_score(dict, is_straight):
    if "Ace" in dict and not is_straight:
        return dict["Ace"]
    elif "King" in dict:
        return dict["King"]
    elif "Queen" in dict:
        return dict["Queen"]
    elif "Jack" in dict:
        return dict["Jack"]
    elif "10" in dict:
        return dict["10"]
    elif "9" in dict:
        return dict["9"]
    elif "8" in dict:
        return dict["8"]
    elif "7" in dict:
        return dict["7"]
    elif "6" in dict:
        return dict["6"]
    elif "5" in dict:
        return dict["5"]
    elif "4" in dict:
        return dict["4"]
    elif "3" in dict:
        return dict["3"]
    elif "2" in dict:
        return dict["2"]
    elif "Ace" in dict:
        return dict["Ace"]
    else:
        Exception("Highest Score Error")

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
        return rank.HIGHEST_CARD

def convert_from_score(type: int) -> str:
    if type == rank.ROYAL_FLUSH:
        return "Royal Flush"
    if type == rank.STRAIGHT_FLUSH:
        return "Straight Flush"
    if type == rank.FOUR_OF_A_KIND:
        return "Four of a Kind"
    if type == rank.FULL_HOUSE:
        return "Full House"
    if type == rank.FLUSH:
        return "Flush"
    if type == rank.STRAIGHT:
        return "Straight"
    if type == rank.THREE_OF_A_KIND:
        return "Three of a Kind"
    if type == rank.TWO_PAIR:
        return "Two Pair"
    if type == rank.PAIR:
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

def value_royal_flush(cards):
    # Guaranteed win
    return "0"

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
                needed_card = str(int(1) + i)
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

def value_straight_flush(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    value = ""
    for card in cards:
        valid = True
        for i in range(1, 5):
            if card.value == "Ace":
                needed_card = str(int(1) + i)
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
            value = card.value
    return value

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

def value_four_kind(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1
    
    # TODO: Clean this up
    four_card = [k for k, v in hash.items() if v == 4]
    highest = "2"
    for card in four_card:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(highest):
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)

    return highest

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

def value_full_house(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    three_cards = [k for k, v in hash.items() if v == 3]
    three_highest = "2"
    for card in three_cards:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(three_highest):
            three_highest = int_card

    if three_highest == 11:
        three_highest = "Jack"
    elif three_highest == 12:
        three_highest = "Queen"
    elif three_highest == 13:
        three_highest = "King"
    elif three_highest == 14:
        three_highest = "Ace"
    else:
        three_highest = str(three_highest)
    
    two_cards = [k for k, v in hash.items() if v == 2]
    two_highest = "2"
    for card in two_cards:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(two_highest):
            two_highest = int_card

    if two_highest == 11:
        two_highest = "Jack"
    elif two_highest == 12:
        two_highest = "Queen"
    elif two_highest == 13:
        two_highest = "King"
    elif two_highest == 14:
        two_highest = "Ace"
    else:
        two_highest = str(two_highest)

    ret = str(three_highest) + " " + str(two_highest)
    return ret

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

def value_flush(cards):
    hash = {}
    for card in cards:
        if card.suit in hash:
            hash[card.suit] += 1
        else:
            hash[card.suit] = 1

    suit = [k for k, v in hash.items() if v == 5]
    
    highest = "2"
    
    for card in cards:
        if card.value == "Jack":
            int_card = 11
        elif card.value == "Queen":
            int_card = 12
        elif card.value == "King":
            int_card = 13
        elif card.value == "Ace":
            int_card = 14
        else:
            int_card = int(card.value)
        if card.suit == suit[0] and int_card >= int(highest):
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)
    return highest

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
                needed_card = str(int(1) + i)
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

def value_straight(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1

    value = ""
    for card in cards:
        valid = True
        for i in range(1, 5):
            if card.value == "Ace":
                needed_card = str(int(1) + i)
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
            value = card.value
    return value

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

def value_three_kind(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1
    
    # TODO: Clean this up
    four_card = [k for k, v in hash.items() if v == 3]
    highest = "2"
    for card in four_card:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(highest):
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)

    return highest

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

def value_two_pair(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1
    
    picked = []

    # TODO: Clean this up
    pair_card = [k for k, v in hash.items() if v == 2]
    highest = "2"
    for card in pair_card:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(highest) and card not in picked:
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)

    picked.append(highest)

    # Second, messy implementation
    # TODO: CLEANUP
    highest = "2"
    for card in pair_card:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(highest) and card not in picked:
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)

    picked.append(highest)

    third = value_high_card(cards, picked)

    ret = str(picked[0]) + " " + str(picked[1] + " " + third)
    
    return ret

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

def value_pair(cards):
    hash = {}
    for card in cards:
        if card.value in hash:
            hash[card.value] += 1
        else:
            hash[card.value] = 1
    
    # TODO: Clean this up
    pair_card = [k for k, v in hash.items() if v == 2]
    highest = "2"
    for card in pair_card:
        int_card = card
        if card == "Jack":
            int_card = 11
        elif card == "Queen":
            int_card = 12
        elif card == "King":
            int_card = 13
        elif card == "Ace":
            int_card = 14
        else:
            int_card = int(card)
        if int_card >= int(highest):
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)

    return highest

def value_high_card(cards, picked):
    highest = "2"
    
    for card in cards:
        int_card = 0
        if card.value == "Jack":
            int_card = 11
        elif card.value == "Queen":
            int_card = 12
        elif card.value == "King":
            int_card = 13
        elif card.value == "Ace":
            int_card = 14
        else:
            int_card = int(card.value)
        if int_card >= int(highest) and card.value not in picked:
            highest = int_card

    if highest == 11:
        highest = "Jack"
    elif highest == 12:
        highest = "Queen"
    elif highest == 13:
        highest = "King"
    elif highest == 14:
        highest = "Ace"
    else:
        highest = str(highest)
    return highest

def is_equal(card1, card2):
    if card1.suit == card2.suit and card1.value == card2.value:
        return True
    return False

def is_card_in(card, array):
    for c in array:
        if is_equal(card, c):
            return True
    return False