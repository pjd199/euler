"""
Project Euler Problem 61
========================

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following
formulae:

Triangle     P[3,n]=n(n+1)/2    1, 3, 6, 10, 15, ...
Square       P[4,n]=n^2         1, 4, 9, 16, 25, ...
Pentagonal   P[5,n]=n(3n-1)/2   1, 5, 12, 22, 35, ...
Hexagonal    P[6,n]=n(2n-1)     1, 6, 15, 28, 45, ...
Heptagonal   P[7,n]=n(5n-3)/2   1, 7, 18, 34, 55, ...
Octagonal    P[8,n]=n(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

 1. The set is cyclic, in that the last two digits of each number is the
    first two digits of the next number (including the last number with
    the first).
 2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281),
    and pentagonal (P[5,44]=2882), is represented by a different number in
    the set.
 3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the
set.
"""

from collections import deque
from itertools import dropwhile, takewhile

from euler.utils.sequences import polygonal


def solution61() -> int:
    # get the 4 digit numbers for each polyagonalsequence, storing as str
    sequences = {
        i: set(
            map(
                str,
                takewhile(
                    lambda x: x < 10000, dropwhile(lambda x: x < 1000, polygonal(i))
                ),
            )
        )
        for i in range(3, 9)
    }
    # create a lookup based on the first two digits of each number
    head_lookup: dict[int, dict[str, set[str]]] = {}
    for rank in sequences:
        for number in sequences[rank]:
            head_lookup.setdefault(rank, {}).setdefault(number[:2], set()).add(number)

    # prepare for the breadth first search
    queue = deque(
        [
            ([number], [rank])
            for rank, lookup in head_lookup.items()
            for head in lookup.values()
            for number in head
        ]
    )
    # perform the search
    while queue:
        numbers, ranks = queue.popleft()

        for rank in head_lookup:
            # ignore duplicate ranks
            if rank not in ranks:
                for number in head_lookup[rank].get(numbers[-1][2:], []):
                    if number not in numbers:
                        possible = [*numbers, number]
                        if len(possible) < 6:
                            # continue the search
                            queue.append((possible, [*ranks, rank]))
                        elif possible[-1][2:] == possible[0][:2]:
                            # found the result
                            return sum(map(int, possible))

    # solution not found
    return 0


if __name__ == "__main__":
    print(solution61())
