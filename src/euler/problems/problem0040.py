"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

from collections.abc import Iterator
from itertools import count, islice
from math import prod

from euler.utils.digits import split_digits


def solution() -> int:
    # iterator for the number sequence
    def seq() -> Iterator[int]:
        yield 0
        for i in count(1):
            yield from split_digits(i)

    # locations to multiply
    locations = {10**x for x in range(7)}
    # return the product of digits in locations
    return prod(x for i, x in enumerate(islice(seq(), 1000001)) if i in locations)


if __name__ == "__main__":
    print(solution())
