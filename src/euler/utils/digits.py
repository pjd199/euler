from collections import Counter
from functools import cache
from itertools import chain


@cache
def split_digits(n: int) -> tuple[int, ...]:
    return tuple(map(int, str(n)))


@cache
def join_digits(digits: tuple[int, ...]) -> int:
    return int("".join(map(str, digits)))


@cache
def count_digits(*args: int) -> int:
    return sum(len(str(x)) for x in args)


@cache
def sum_digits(*args: int) -> int:
    return sum(sum(split_digits(x)) for x in args)


@cache
def reverse_digits(n: int) -> int:
    return int(str(n)[::-1])


@cache
def pandigital(*args: int) -> bool:
    counter = Counter(chain.from_iterable(split_digits(n) for n in args))
    return all(v == 1 for v in counter.values()) and all(
        n in counter for n in range(1, len(counter) + 1)
    )


@cache
def palindrome2(n: int) -> bool:
    s = f"{n:b}"
    return s == s[::-1]


@cache
def palindrome8(n: int) -> bool:
    s = f"{n:o}"
    return s == s[::-1]


@cache
def palindrome10(n: int) -> bool:
    s = f"{n:d}"
    return s == s[::-1]


@cache
def palindrome16(n: int) -> bool:
    s = f"{n:x}"
    return s == s[::-1]


@cache
def is_anagram(a: int, b: int) -> bool:
    return sorted(str(a)) == sorted(str(b))
