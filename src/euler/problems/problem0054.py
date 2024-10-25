"""
Project Euler Problem 54
========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?
"""

from collections import Counter
from dataclasses import dataclass

card_values_decoder = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


@dataclass
class Card:
    def __init__(self, card: str) -> None:
        self.value = card_values_decoder[card[0]]
        self.suit = card[1]

    value: str
    suit: str


def rank(hand: list[Card]) -> tuple[int, int, int]:
    values = sorted([x.value for x in hand])
    values_counter = Counter(values)
    highest = max(values)
    suits = sorted([x.suit for x in hand])
    suits_counter = Counter(suits)

    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if values == [10, 11, 12, 13, 14]:
        return (10, 14, highest)

    # Straight Flush: All cards are consecutive values of same suit.
    if all(x == suits[0] for x in suits) and all(
        values[i] + 1 == values[i + 1] for i in range(len(values) - 1)
    ):
        return (9, highest, highest)

    # Four of a Kind: Four cards of the same value.
    if max(values_counter.values()) >= 4:
        return (
            8,
            max(value for value, count in values_counter.items() if count >= 4),
            highest,
        )

    # Full House: Three of a kind and a pair.
    if set(values_counter.values()) == {2, 3}:
        return (7, highest, highest)

    # Flush: All cards of the same suit.
    if len(set(suits_counter.values())) == 1:
        return (6, highest, highest)

    # Straight: All cards are consecutive values.
    if all(values[i] + 1 == values[i + 1] for i in range(len(values) - 1)):
        return (5, highest, highest)

    # Three of a Kind: Three cards of the same value.
    if max(values_counter.values()) >= 3:
        return (
            4,
            max(value for value, count in values_counter.items() if count >= 3),
            highest,
        )

    # Two Pairs: Two different pairs.
    if sorted(values_counter.values()) == [1, 2, 2]:
        return (
            3,
            max(value for value, count in values_counter.items() if count == 2),
            highest,
        )

    # One Pair: Two cards of the same value.
    if max(values_counter.values()) >= 2:
        return (
            2,
            max(value for value, count in values_counter.items() if count == 2),
            highest,
        )

    # High Card: Highest value card.
    return (1, highest, highest)


def solution() -> int:
    with open("./resources/poker.txt") as file:
        lines = [[Card(x) for x in line.split(" ")] for line in file.readlines()]

    return sum(1 for cards in lines if rank(cards[:5]) > rank(cards[5:]))


if __name__ == "__main__":
    print(solution())
