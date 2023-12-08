from collections import Counter


def hand_score(hand, hand_with_joker, cards_order):
    hand_type = "".join(
        map(str, sorted(Counter(hand_with_joker).values(), reverse=True))
    ).ljust(5, "0")
    cards_points = dict(zip(cards_order, range(len(cards_order))))
    cards_scores = "".join(str(cards_points[c]).rjust(2, "0") for c in hand)
    return hand_type + cards_scores


def score(hand, cards_order="23456789TJQKA"):
    return hand_score(hand, hand, cards_order)


def score_with_joker(hand, cards_order="J23456789TQKA"):
    hand_with_joker = sorted(
        [hand.replace("J", c) for c in set(hand) - {"J"}] or ["AAAAA"], key=score
    )[-1]
    return hand_score(hand, hand_with_joker, cards_order)


def winnings(hands, bids, key):
    hands2bids = dict(zip(hands, bids))
    return [
        i * int(hands2bids[hand]) for i, hand in enumerate(sorted(hands, key=key), 1)
    ]


with open("data") as f:
    hands, bids = zip(*map(str.split, f.read().splitlines()))


# ========== PART 1 ===========
print(sum(winnings(hands, bids, score)))

# ========== PART 2 ===========
print(sum(winnings(hands, bids, score_with_joker)))
