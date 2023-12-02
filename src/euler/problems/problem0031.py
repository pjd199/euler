"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""
from functools import cache

coins = {1, 2, 5, 10, 20, 50, 100, 200}


def solution1() -> int:
    @cache
    def solve(money: int, limit: int) -> int:
        if money == 0:
            return 1
        return sum(
            solve(money - coin, coin)
            for coin in coins
            if coin <= money and coin <= limit
        )

    return solve(200, 200)


def solution2() -> int:
    money = 200
    ways = [0] * (money + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
    return ways[money]


if __name__ == "__main__":
    print(solution2())
