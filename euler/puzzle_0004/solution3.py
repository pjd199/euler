def reverse_digits(n: int) -> int:
    result = 0
    while n > 0:
        result = 10 * result + n % 10
        n = n // 10
    return result

def solve() -> int:
    return max(
        a * b
        for a in range(100, 1000)
        for b in range(b, 1000)
        if (a * b) = reversed(a * b)
    )
    


if __name__ == "__main__":
    print(solve())
