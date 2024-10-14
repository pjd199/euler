"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""
from itertools import count
from math import gcd


def solution() -> int:
    # find the primitive Pythagorean triples using Euclid's formula
    limit = 100
    primitive_triples = (
        (m**2 - n**2, 2 * m * n, m**2 + n**2)
        for n in range(1, limit)
        for m in range(n + 1, limit)
        if (
            ((n % 2 == 0 and m % 2 == 1) or (n % 2 == 1 and m % 2 == 0))
            and gcd(n, m) == 1
        )
    )

    # count the parimeters of the triples, multiplying triples
    perimeters = [0 for _ in range(1001)]
    for triple in primitive_triples:
        p = sum(triple)
        for i in count(1):
            if (p * i) <= 1000:
                perimeters[p * i] += 1
            else:
                break

    return perimeters.index(max(perimeters))


if __name__ == "__main__":
    print(solution())
