"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

from euler.utils.right_angle_triangles import perimeter_counter


def solution() -> int:
    return max(
        (count, perimeter) for perimeter, count in perimeter_counter(1000).items()
    )[1]


if __name__ == "__main__":
    print(solution())
