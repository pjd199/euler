"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from euler.utils.primes import prime_generator


def solution() -> int:
    limit = 1000000
    prime_list = list(prime_generator(limit))
    prime_set = set(prime_list)
    max_length = 0
    max_prime = 0

    for i in range(len(prime_list)):
        for j in range(i + max_length, len(prime_list)):
            prime_sum = sum(prime_list[i:j])
            if prime_sum >= limit:
                break
            if prime_sum in prime_set:
                max_length = j - i
                max_prime = prime_sum

    return max_prime


if __name__ == "__main__":
    print(solution())
