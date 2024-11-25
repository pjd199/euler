"""
Project Euler Problem 75
========================

It turns out that 12 cm is the smallest length of wire can be bent to form
a right angle triangle in exactly one way, but there are many more
examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form a
right angle triangle, and other lengths allow more than one solution to be
found; for example, using 120 cm it is possible to form exactly three
different right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L 2,000,000
can exactly one right angle triangle be formed?
"""

from euler.utils.right_angle_triangles import perimeter_counter


def solution0075() -> int:
    return sum(1 for x in perimeter_counter(1500000).values() if x == 1)


if __name__ == "__main__":
    print(solution0075())
