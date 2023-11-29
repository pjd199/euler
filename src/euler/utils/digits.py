from collections import Counter
from functools import cache
from itertools import chain
from math import floor, log10


@cache
def split_digits(n: int) -> list[int]:
    return [(n // (10**i)) % 10 for i in range(floor(log10(n)), -1, -1)]


@cache
def pandigital(*args: int) -> bool:
    counter = Counter(chain.from_iterable(split_digits(n) for n in args))
    return all(v == 1 for v in counter.values()) and all(
        n in counter for n in range(1, len(counter) + 1)
    )
