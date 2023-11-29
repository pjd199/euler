"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
from collections import Counter
from math import gcd
from euler.utils.digits import split_digits


def solution1() -> int:
    numerator = 1
    denominator = 1
    for a in range(10, 100):
        for b in range(a, 100):
            digits_a = split_digits(a)
            digits_b = split_digits(b)
            counter = Counter(digits_a)
            counter.update(digits_b)
            if (
                len(counter) == 3
                and a % 11 != 0
                and b % 11 != 0
                and a % 10 != 0
                and b % 10 != 0
            ):
                digits_a = [x for x in digits_a if counter[x] == 1]
                digits_b = [x for x in digits_b if counter[x] == 1]
                if (a / b) == (digits_a[0] / digits_b[0]):
                    numerator *= digits_a[0]
                    denominator *= digits_b[0]
    return denominator // gcd(numerator, denominator)


def solution2() -> int:
    numerator = 1
    denominator = 1
    for a in range(10, 100):
        for b in range(a, 100):
            singles = [x for x in split_digits(a) if x not in split_digits(b)] + [
                x for x in split_digits(b) if x not in split_digits(a)
            ]
            if len(singles) == 2 and a % 10 != 0 and b % 10 != 0 and (a / b) == (singles[0] / singles[1]):
                numerator *= singles[0]
                denominator *= singles[1]
    return denominator // gcd(numerator, denominator)


if __name__ == "__main__":
    print(solution2())
