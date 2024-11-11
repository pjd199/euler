"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
from functools import cache
from math import ceil, factorial


@cache
def pascal(n: int, k: int) -> int:
    if n == 0 or k == 0 or n == k:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)


def solution1() -> int:
    n = 20
    return pascal(2 * n, n)


def solution2() -> int:
    n = 20
    return factorial(2 * n) // ((factorial(n)) * factorial(2 * n - n))


def solution3() -> int:
    n = 20
    result = 1.0
    for i in range(1, n + 1):
        result *= (n + i) / i
    return ceil(result)


if __name__ == "__main__":
    print(solution3())
