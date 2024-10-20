"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from euler.utils.primes import prime_generator


def solution() -> int:
    n = 600851475143
    primes = prime_generator()
    prime = next(primes)
    while n > 1:
        if n % prime == 0:
            n = n // prime
        else:
            prime = next(primes)
    return prime


if __name__ == "__main__":
    print(solution())
