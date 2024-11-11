"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
from itertools import islice
from math import sqrt
from operator import itemgetter

from euler.utils.continued_fractions import convergents, square_root


def find_x_and_y(d: int) -> tuple[int, int]:
    # solving Pell's equations
    # https://en.wikipedia.org/wiki/Pell%27s_equation#Example
    whole, cycle = square_root(d)
    n = len(cycle) - 1 if len(cycle) % 2 == 0 else 2 * len(cycle) - 1
    fraction = next(islice(convergents(whole, cycle), n, n + 1))
    return fraction.as_integer_ratio()


def solution66() -> int:
    return max(
        ((d, find_x_and_y(d)) for d in range(1001) if not sqrt(d).is_integer()),
        key=itemgetter(1),
    )[0]


if __name__ == "__main__":
    print(solution66())
