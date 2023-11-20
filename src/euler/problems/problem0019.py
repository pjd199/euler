"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""


def solution1() -> int:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 1
    result = 0
    for year in range(1901, 2001):
        days_in_month[1] = (
            29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28
        )
        for month in range(12):
            day = (day + days_in_month[month]) % 7
            if day % 7 == 6:
                result += 1
    return result


def zellers_congruence(day: int, month: int, year: int) -> int:
    """Uses Zeller's Congruence to calculate day of the week."""
    q = day
    m = month + 12
    y = year - 1
    return (q + ((13 * (m + 1)) // 5) + y + (y // 4) - (y // 100) + (y // 400)) % 7


def solution2() -> int:
    return sum(
        1
        for year in range(1901, 2001)
        for month in range(1, 13)
        if zellers_congruence(1, month, year) == 1
    )


if __name__ == "__main__":
    print(solution2())
