from collections.abc import Iterator

def fibonacci() -> Iterator[int]:
    a = 1
    b = 2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

