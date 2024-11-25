from collections import Counter
from math import gcd, sqrt


def primitive_pythagorean_triples(max_perimeter: int) -> set[tuple[int, int, int]]:
    return {
        (a, b, c)
        for a, b, c in (
            tuple(sorted((m * n, (m**2 - n**2) // 2, (m**2 + n**2) // 2)))
            for m in range(1, int(sqrt(max_perimeter)) + 1, 2)
            for n in range(1, m, 2)
            if gcd(m, n) == 1
        )
        if a + b + c <= max_perimeter
    }


def pythagorean_triples(max_perimeter: int) -> set[tuple[int, int, int]]:
    return {
        (k * a, k * b, k * c)
        for a, b, c in primitive_pythagorean_triples(max_perimeter)
        for k in range(1, (max_perimeter // (a + b + c)) + 1)
    }


def perimeter_counter(max_perimeter: int) -> dict[int, int]:
    return Counter(
        (
            a + b + c
            for a, b, c in pythagorean_triples(max_perimeter)
            if a + b + c <= max_perimeter
        )
    )
