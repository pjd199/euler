from math import floor, log10

def split_digits(n: int) -> list[int]:
    return [
        (n // (10 ** i)) % 10
        for i in range(floor(log10(n)), -1, -1)
    ]
