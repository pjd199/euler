"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def solution1() -> int:
    return sum(int(x)
        for x in str(2 ** 1000)
    )

def solution2() -> int:
    n = 2 ** 1000
    result = 0
    while n > 0:
        result += (n % 10)
        n //= 10
    return result

if __name__ == "__main__":
    print(solution2())
