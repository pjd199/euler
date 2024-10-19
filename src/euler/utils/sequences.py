from collections.abc import Iterator
from itertools import count


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
