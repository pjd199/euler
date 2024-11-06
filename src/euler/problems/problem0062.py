"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""

from itertools import count


def solution62() -> int:
    counter: dict[str, list[int]] = {}
    for i in count():
        cube = "".join(sorted(str(i**3)))
        counter.setdefault(cube, []).append(i)
        if len(counter[cube]) == 5:
            return min(counter[cube]) ** 3

    return -1  # pragma: no cover


if __name__ == "__main__":
    print(solution62())
