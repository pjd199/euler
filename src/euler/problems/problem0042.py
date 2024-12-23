"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from itertools import takewhile

from euler.utils.sequences import polygonal


def load_words() -> list[str]:
    with open("./resources/words.txt") as file:
        return [name.strip('"') for name in file.read().split(",")]


def word_value(word: str) -> int:
    return sum(ord(letter) - ord("A") + 1 for letter in word)


def solution() -> int:
    values = [word_value(word) for word in load_words()]
    max_value = max(values)
    triangular_numbers = set(takewhile(lambda n: n <= max_value, polygonal(side=3)))
    return sum(1 for value in values if value in triangular_numbers)


if __name__ == "__main__":
    print(solution())
