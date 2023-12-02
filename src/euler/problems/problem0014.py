"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from functools import cache


@cache
def collatz_length(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_length(n // 2)
    return 1 + collatz_length((3 * n) + 1)


def solution1() -> int:
    return max((collatz_length(i), i) for i in range(1000000))[1]


def solution2() -> int:
    return max((collatz_length(i), i) for i in range(500000, 1000000))[1]


if __name__ == "__main__":
    print(solution2())
