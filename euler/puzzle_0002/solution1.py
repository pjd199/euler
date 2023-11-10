from collections.abc import Iterator
from itertools import takewhile

def fibonacci() -> Iterator[int]:
    a = 1
    b = 2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def solve() -> int:
    return sum(
        x
        for x in takewhile(lambda n: n < 4000000, fibonacci())
        if x % 2 == 0

    )


if __name__ == "__main__":
    print(solve())
