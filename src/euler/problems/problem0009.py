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

from euler.utils.right_angle_triangles import pythagorean_triples


def solution0009() -> int:
    a, b, c = next(
        (a, b, c) for a, b, c in pythagorean_triples(1000) if a + b + c == 1000
    )
    return a * b * c


if __name__ == "__main__":
    print(solution0009())
