"""
Project Euler Problem 70
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""

from itertools import product
from operator import itemgetter

from euler.utils.digits import is_anagram
from euler.utils.euler_totient import totient
from euler.utils.primes import sieve_of_eratosthenes


def solution0070() -> int:
    return min(
        (
            (n / phi, n)
            for n, phi in (
                (a * b, totient(a) * totient(b))
                for a, b in product(sieve_of_eratosthenes(10000), repeat=2)
                if a * b < 10000000 and is_anagram(a * b, totient(a) * totient(b))
            )
        ),
        key=itemgetter(0),
    )[1]


if __name__ == "__main__":
    print(solution0070())
