"""
Project Euler Problem 76
========================

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""

from functools import cache


@cache
def summation(n: int, high: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(summation(n - x, x) for x in range(1, high + 1))


def solution0076() -> int:
    return summation(100, 99)


if __name__ == "__main__":
    print(solution0076())
