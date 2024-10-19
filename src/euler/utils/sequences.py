from collections.abc import Iterator
from itertools import count
from math import sqrt


def fibonacci() -> Iterator[int]:
    a = 1
    b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def triangular() -> Iterator[int]:
    for n in count(1):
        yield (n * (n + 1)) // 2


def is_triagular(n: int) -> bool:
    return ((sqrt(8 * n + 1) - 1) / 2).is_integer()


def pentagonal() -> Iterator[int]:
    for n in count(1):
        yield (n * (3 * n - 1)) // 2


def is_pentagonal(n: int) -> bool:
    return ((sqrt(24 * n + 1) + 1) / 6).is_integer()


def hexagonal() -> Iterator[int]:
    for n in count(1):
        yield n * (2 * n - 1)


def is_hexagonal(n: int) -> bool:
    return ((sqrt(8 * n + 1) + 1) / 4).is_integer()
