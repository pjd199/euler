"""
Project Euler Problem 44
========================

Pentagonal numbers are generated by the formula, P[n]=n(3n-1)/2. The first
ten pentagonal numbers are:

               1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P[4] + P[7] = 22 + 70 = 92 = P[8]. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P[j] and P[k], for which their sum
and difference is pentagonal and D = |P[k] - P[j]| is minimised; what is
the value of D?
"""

from itertools import combinations, takewhile

from euler.utils.sequences import polygonal


def solution() -> int:
    pentagonals = set(takewhile(lambda n: n < 10000000, polygonal(side=5)))
    return min(
        abs(a - b)
        for a, b in combinations(pentagonals, 2)
        if (a + b) in pentagonals and abs(a - b) in pentagonals
    )


if __name__ == "__main__":
    print(solution())
