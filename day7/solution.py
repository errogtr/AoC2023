from collections import Counter
from copy import copy

HAND_TYPES = {"11111": 0, "1112": 1, "122": 2, "113": 3, "23": 4, "14": 5, "5": 6}


def get_cards_order(suits):
    return dict(zip(suits, range(len(suits))))


def hand_type(hand):
    return "".join(map(str, sorted(Counter(hand).values())))


def hand_type_with_joker(hand):
    if "J" not in hand:
        return HAND_TYPES[hand_type(hand)]
    if hand.count("J") == len(hand):
        return HAND_TYPES[str(len(hand))]
    return max(HAND_TYPES[hand_type(hand.replace("J", h))] for h in set(hand) - {"J"})


def sort_hand(card, cards_order):
    return cards_order[card]


def swap(left, right, cards_order):
    type_left = HAND_TYPES[hand_type(left)]
    type_right = HAND_TYPES[hand_type(right)]
    if type_left > type_right:
        return True
    if type_left == type_right:
        for x, y in zip(left, right):
            if cards_order[x] > cards_order[y]:
                return True
            if cards_order[x] < cards_order[y]:
                return False
    return False


def swap_with_joker(left, right, cards_order):
    type_left = hand_type_with_joker(left)
    type_right = hand_type_with_joker(right)
    if type_left > type_right:
        return True
    if type_left == type_right:
        for x, y in zip(left, right):
            if cards_order[x] > cards_order[y]:
                return True
            if cards_order[x] < cards_order[y]:
                return False
    return False


with open("data") as f:
    all_hands = [x.split() for x in f.read().splitlines()]

cards_order = get_cards_order("23456789TJQKA")
sorted_hands = copy(all_hands)
n_hands = len(sorted_hands)
for i in range(n_hands):
    for j in range(n_hands - i - 1):
        left = sorted_hands[j][0]
        right = sorted_hands[j + 1][0]
        if swap(left, right, cards_order):
            sorted_hands[j], sorted_hands[j + 1] = sorted_hands[j + 1], sorted_hands[j]


print(sum(i * int(bid) for i, (hand, bid) in enumerate(sorted_hands, 1)))


cards_order = get_cards_order("J23456789TQKA")
sorted_hands = copy(all_hands)
n_hands = len(sorted_hands)
for i in range(n_hands):
    for j in range(n_hands - i - 1):
        left = sorted_hands[j][0]
        right = sorted_hands[j + 1][0]
        if swap_with_joker(left, right, cards_order):
            sorted_hands[j], sorted_hands[j + 1] = sorted_hands[j + 1], sorted_hands[j]

print(sum(i * int(bid) for i, (hand, bid) in enumerate(sorted_hands, 1)))
