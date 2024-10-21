"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from euler.utils.digits import join_digits, split_digits
from euler.utils.primes import prime_generator


def solution() -> int:
    step = 3330
    prime_list = {x for x in prime_generator(10000) if x > 1000}
    triples = {
        (x, x + step, x + 2 * step)
        for x in prime_list
        if (x + step) in prime_list
        and (x + 2 * step) in prime_list
        and set(split_digits(x))
        == set(split_digits(x + step))
        == set(split_digits(x + 2 * step))
    }
    triples.remove((1487, 4817, 8147))
    x, y, z = triples.pop()
    return join_digits(tuple(split_digits(x) + split_digits(y) + split_digits(z)))


if __name__ == "__main__":
    print(solution())
