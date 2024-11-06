"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

from euler.utils.resources import load_resource


def load_names() -> list[str]:
    return [name.strip('"') for name in load_resource("names").split(",")]


def alphabetical_value(word: str) -> int:
    return sum(ord(x) - ord("A") + 1 for x in word)


def solution1() -> int:
    names = {
        name: i + 1
        for i, name in enumerate(
            sorted([name.strip('"') for name in load_resource("names").split(",")])
        )
    }
    return sum(alphabetical_value(name) * names[name] for name in names)


if __name__ == "__main__":
    print(solution1())
