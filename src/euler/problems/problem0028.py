"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""
from collections.abc import Iterator
from itertools import count, takewhile


def corner_values() -> Iterator[int]:
    yield 1
    width = 1
    n = 1
    for step in count():
        if step % 4 == 0:
            width += 2
        n += width - 1
        yield n


def solution1() -> int:
    return sum(takewhile(lambda x: x <= 1001**2, corner_values()))


if __name__ == "__main__":
    print(solution1())
