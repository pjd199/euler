"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from functools import cache

from euler.utils.factorization import proper_factors, sum_of_factors


def solution1() -> int:
    sums = {i: sum(proper_factors(i)) for i in range(1, 10000)}
    amicable = {a for a, b in sums.items() if a != b and b in sums and a == sums[b]}
    return sum(amicable)


def solution2() -> int:
    sums = {i: (sum_of_factors(i) - i) for i in range(1, 10000)}
    amicable = {a for a, b in sums.items() if a != b and b in sums and a == sums[b]}
    return sum(amicable)


def solution3() -> int:
    numbers = {i for i in range(1, 10000)}
    amicable = set()
    while numbers:
        a = numbers.pop()
        b = sum(proper_factors(a))
        if b in numbers and a == sum(proper_factors(b)):
            amicable.add(a)
            amicable.add(b)
            numbers.discard(b)
    return sum(amicable)


def solution4() -> int:
    result = 0
    for a in range(2, 10000):
        b = sum(proper_factors(a))
        if b > a and a == sum(proper_factors(b)):
            result += a + b
    return result


@cache
def sum_proper_factors(n: int) -> int:
    return sum(proper_factors(n))


def solution5() -> int:
    return sum(
        a + sum_proper_factors(a)
        for a in range(1, 10000)
        if a < sum_proper_factors(a) and a == sum_proper_factors(sum_proper_factors(a))
    )


if __name__ == "__main__":
    print(solution5())
