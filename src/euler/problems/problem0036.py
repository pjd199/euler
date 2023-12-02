"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
from euler.utils.digits import palindrome2, palindrome10


def solution1() -> int:
    return sum(n for n in range(1000000) if palindrome2(n) and palindrome10(n))


if __name__ == "__main__":
    print(solution1())
