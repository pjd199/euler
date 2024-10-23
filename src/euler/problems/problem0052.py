"""
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

from itertools import count

from euler.utils.digits import split_digits


def solution() -> int:
    return next(
        x
        for x in count(1)
        if set(split_digits(x))
        == set(split_digits(2 * x))
        == set(split_digits(3 * x))
        == set(split_digits(2 * x))
        == set(split_digits(5 * x))
        == set(split_digits(6 * x))
    )


if __name__ == "__main__":
    print(solution())
