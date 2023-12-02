"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution1() -> int:
    """First solution.

    The brute force approach.
    """
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)


def solution2() -> int:
    """Second solution.

    A little more sophiticated, calculating the sum of
    (sum of all multiples of 3)
    + (sum of all multiples of 5)
    - (sum of all multiples of (3 * 5))
    """
    threshold = 1000

    def sum_multiples_of(n: int) -> int:
        p = (threshold - 1) // n
        return n * (p * (p + 1)) // 2

    return sum_multiples_of(3) + sum_multiples_of(5) - sum_multiples_of(15)


if __name__ == "__main__":
    print(solution2())
