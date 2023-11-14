"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import ceil, gcd, sqrt


def solution1() -> int:
    target = 1000
    return next(
        a * b * c
        for a in range(1, target)
        for b in range(a + 1, target)
        for c in range(b + 1, target)
        if (a + b + c) == target and a**2 + b**2 == c**2
    )


def solution2() -> int:
    target = 1000
    return next(
        a * b * (target - a - b)
        for a in range(1, target)
        for b in range(a + 1, target)
        if (target - a - b) ** 2 == a**2 + b**2
    )


def solution3() -> int:
    s = 1000
    return next(
        a * b * (s - a - b)
        for a in range(1, (s - 3) // 3)
        for b in range(a + 1, (s - 1 - a) // 2)
        if (s - a - b) ** 2 == a**2 + b**2
    )


def solution4() -> int:
    s = 1000
    s2 = s // 2
    mlimit = ceil(sqrt(s2)) - 1
    for m in range(2, mlimit):
        if s2 % m == 0:
            sm = s2 // m
            while sm % 2 == 0:
                sm //= 2
            k = (m + 2) if (m % 2 == 1) else (m + 1)
            while k < 2 * m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2 // (k * m)
                    n = k - m
                    a = d * (m**2 - n**2)
                    b = 2 * d * m * n
                    c = d * (m**2 + n**2)
                    return a * b * c
                k += 2
    return -1


if __name__ == "__main__":
    print(solution4())
