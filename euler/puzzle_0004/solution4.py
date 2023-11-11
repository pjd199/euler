def reverse_digits(n: int) -> int:
    result = 0
    while n > 0:
        result = 10 * result + n % 10
        n = n // 10
    return result


def solve() -> int:
    largest = 0
    for a in range(999, 99, -1):
        start, step = (999, -1) if a % 11 == 0 else (990, -11)
        for b in range(start, a - 1, step):
            ab = a * b
            if ab < largest:
                break
            if ab == reverse_digits(ab):
                largest = ab

    return largest


if __name__ == "__main__":
    print(solve())
