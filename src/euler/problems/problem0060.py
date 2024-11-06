"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from euler.utils.primes import is_prime, sieve_of_eratosthenes


def find(primes: list[int], current: list[int], size: int) -> list[int]:
    # found the solution
    if len(current) == size:
        return current

    # minimise the search space by search larger primes
    if len(current) > 0:
        primes = primes[primes.index(current[-1]) + 1 :]

    # try and find the next possible prime
    for prime in primes:
        if all(
            is_prime(int(str(prime) + str(x))) and is_prime(int(str(x) + str(prime)))
            for x in current
        ):
            result = find(primes, [*current, prime], size)
            if result:
                return result
    return []  # pragma: no cover


def solution60() -> int:
    return sum(find(sieve_of_eratosthenes(10000), [], 5))


if __name__ == "__main__":
    print(solution60())
