"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
from itertools import product
from euler.utils.prime_list import primes


def longest_quadratic_primes_sequence(a: int, b: int) -> int:
    n = 0
    while ((n**2) + (a * n) + b) in primes:
        n += 1

    return n


def solution1() -> int:
    coef_a = [-x for x in primes if x < 1000]
    coef_b = [x for x in primes if x < 1000]

    longest = 0
    result = 0
    for a, b in product(coef_a, coef_b):
        if (longest**2) + (a * longest) + b in primes:
            length = longest_quadratic_primes_sequence(a, b)
            if length > longest:
                longest = length
                result = a * b
    return result

    # return max(
    #     (longest_quadratic_primes_sequence(a, b), a * b)
    #     for a in coef
    #     for b in coef
    # )[1]


if __name__ == "__main__":
    print(solution1())
