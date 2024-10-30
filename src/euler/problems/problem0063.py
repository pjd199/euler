"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from euler.utils.digits import count_digits


def solution63() -> int:
    return sum(
        1 for i in range(1, 100) for n in range(1, 100) if count_digits(i**n) == n
    )


if __name__ == "__main__":
    print(solution63())
