"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""
from math import factorial
from euler.utils.digits import split_digits


def solution1() -> int:
    return sum(split_digits(factorial(100)))


if __name__ == "__main__":
    print(solution1())
