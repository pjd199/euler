def palindrome(n: int) -> bool:
    s = str(n)
    return s[: len(s) // 2] == s[-1 : -len(s) // 2 - (1 if len(s) % 2 == 0 else 0) : -1]


def solve() -> int:
    return max(
        a * b
        for a in range(100, 1000)
        for b in range(100, 1000)
        if palindrome(a * b)
    )
    


if __name__ == "__main__":
    print(solve())
