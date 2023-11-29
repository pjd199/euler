"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from euler.utils.digits import palindrome10


def solution1() -> int:
    return max(
        a * b for a in range(100, 1000) for b in range(100, 1000) if palindrome10(a * b)
    )


def solution2() -> int:
    return max(
        a * b for a in range(100, 1000) for b in range(a, 1000) if palindrome10(a * b)
    )


def solution3() -> int:
    largest = 0
    for a in range(999, 99, -1):
        start, step = (999, -1) if a % 11 == 0 else (990, -11)
        for b in range(start, a - 1, step):
            if (a * b) < largest:
                break
            if palindrome10(a * b):
                largest = a * b

    return largest


if __name__ == "__main__":
    print(solution3())
