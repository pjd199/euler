"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def solution1() -> int:
    return sum(range(1, 101)) ** 2 - sum(x**2 for x in range(1, 101))


def solution2() -> int:
    n = 100
    square_of_sum = (n * (n + 1) // 2) ** 2
    sum_of_squares = (2 * n + 1) * (n + 1) * n // 6
    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    print(solution2())
