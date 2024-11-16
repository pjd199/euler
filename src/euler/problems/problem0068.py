"""
Project Euler Problem 68
========================

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.

Working clockwise, and starting from the group of three with the
numerically lowest external node (4,3,2 in this example), each solution
can be described uniquely. For example, the above solution can be
described by the set: 4,3,2; 6,2,1; 5,1,3.

It is new to complete the ring with four different totals: 9, 10, 11,
and 12. There are eight solutions in total.

        Total          Solution Set
        9              4,2,3; 5,3,1; 6,1,2
        9              4,3,2; 6,2,1; 5,1,3
        10             2,3,5; 4,5,1; 6,1,3
        10             2,5,3; 6,3,1; 4,1,5
        11             1,4,6; 3,6,2; 5,2,4
        11             1,6,4; 5,4,2; 3,2,6
        12             1,5,6; 2,6,4; 3,4,5
        12             1,6,5; 3,5,4; 2,4,6

By concatenating each group it is new to form 9-digit strings; the
maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is new
to form 16- and 17-digit strings. What is the maximum 16-digit string for
a "magic" 5-gon ring?
"""

from collections.abc import Iterator


def _gons_iterator(
    ring: list[int], numbers: set[int], index: int, overlap: dict[int, int]
) -> Iterator[str]:
    # test different numbers
    for number in numbers:
        new_ring = ring.copy()
        new_numbers = numbers - {number}
        new_ring[index] = number

        # add any overlaps
        if index in overlap:
            new_ring[overlap[index]] = number

        # validate start of triplets
        if index > 0 and index % 3 == 0 and number < new_ring[0]:
            continue

        # are there more numbers to fit
        if len(new_numbers) > 0:
            yield from _gons_iterator(new_ring, new_numbers, new_ring.index(0), overlap)
        else:
            # validate sum of triplets
            if all(
                sum(new_ring[0:3]) == sum(new_ring[i : i + 3])
                for i in range(3, len(new_ring), 3)
            ):
                # goal
                yield "".join(map(str, new_ring))


def gons(sides: int) -> Iterator[str]:
    yield from _gons_iterator(
        [0] * (sides * 3),
        set(range(1, sides * 2 + 1)),
        0,
        {1: (3 * sides) - 1} | {i: i + 2 for i in range(2, (3 * sides) - 1, 3)},
    )


def solution0068() -> int:
    return max(map(int, (x for x in gons(5) if len(x) == 16)))


if __name__ == "__main__":
    print(solution0068())
