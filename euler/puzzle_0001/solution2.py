def sum_divisable_by(target: int, n: int) -> int:
    p = target // n
    return n * (p * (p + 1)) // 2


def solve() -> int:
    return (
        sum_divisable_by(999, 3) + sum_divisable_by(999, 5) - sum_divisable_by(999, 15)
    )


if __name__ == "__main__":
    print(solve())
