from collections.abc import Iterator
from itertools import count


def prime_numbers() -> Iterator[int]:
    primes = {2}
    yield 2

    def has_prime_factors(n):
        for prime in primes:
            if n % prime == 0:
                return True
        return False

    for n in count(3, 2):
        if not has_prime_factors(n):
            primes.add(n)
            yield n


def solve() -> int:
    n = 600851475143
    prime_iterator = prime_numbers()
    prime = next(prime_iterator)
    while n > 1:
        if n % prime == 0:
            n = n // prime
        else:
            prime = next(prime_iterator)
    return prime

if __name__ == "__main__":
    print(solve())
