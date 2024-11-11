from collections import deque
from collections.abc import Iterator
from fractions import Fraction
from functools import cache
from itertools import cycle
from math import sqrt


@cache
def square_root(n: int) -> tuple[int, tuple[int, ...] | tuple[()]]:
    if sqrt(n).is_integer():
        return (int(sqrt(n)), ())
    m = 0
    d = 1
    a0 = int(sqrt(n))
    a = a0
    end = 2 * a
    digits = []
    while a < end:
        m = d * a - m
        d = (n - m**2) // d
        a = (a0 + m) // d
        digits.append(a)
    return (a0, tuple(digits))


def convergents(whole: int, denominators: tuple[int, ...]) -> Iterator[Fraction]:
    yield Fraction(whole)
    p = deque([1, whole], maxlen=3)
    q = deque([0, 1], maxlen=3)
    for a in cycle(denominators):
        p.append((a * p[-1]) + p[-2])
        q.append((a * q[-1]) + q[-2])
        yield Fraction(p[-1], q[-1])
