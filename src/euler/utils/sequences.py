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


def polygonal(side: int) -> Iterator[int]:
    for n in count(1):
        yield (((side - 2) * n**2) - ((side - 4) * n)) // 2


def is_polygonal(n: int, side: int) -> bool:
    return (
        (sqrt((8 * (side - 2) * n) + (side - 4) ** 2) + (side - 4)) / (2 * (side - 2))
    ).is_integer()
