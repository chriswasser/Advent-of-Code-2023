#!/usr/bin/env python3

import fileinput
from itertools import takewhile
from math import prod
import string

from rich import print
from rich.traceback import install

install(show_locals=True)


def find_numbers(lines: list[str], rindex: int, cindex: int) -> dict[tuple[int, int], int]:
    ret: dict[tuple[int, int], int] = {}

    column = cindex - 1
    while lines[rindex - 1][column].isdigit() and lines[rindex - 1][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex - 1][column:]))
    if numstr:
        ret[rindex - 1, column] = int(numstr)

    column = cindex
    while lines[rindex - 1][column].isdigit() and lines[rindex - 1][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex - 1][column:]))
    if numstr:
        ret[rindex - 1, column] = int(numstr)

    column = cindex + 1
    while lines[rindex - 1][column].isdigit() and lines[rindex - 1][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex - 1][column:]))
    if numstr:
        ret[rindex - 1, column] = int(numstr)

    column = cindex - 1
    while lines[rindex][column].isdigit() and lines[rindex][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex][column:]))
    if numstr:
        ret[rindex, column] = int(numstr)

    column = cindex + 1
    while lines[rindex][column].isdigit() and lines[rindex][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex][column:]))
    if numstr:
        ret[rindex, column] = int(numstr)

    column = cindex - 1
    while lines[rindex + 1][column].isdigit() and lines[rindex + 1][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex + 1][column:]))
    if numstr:
        ret[rindex + 1, column] = int(numstr)

    column = cindex
    while lines[rindex + 1][column].isdigit() and lines[rindex + 1][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex + 1][column:]))
    if numstr:
        ret[rindex + 1, column] = int(numstr)

    column = cindex + 1
    while lines[rindex + 1][column].isdigit() and lines[rindex + 1][column - 1].isdigit():
        column -= 1
    numstr = "".join(takewhile(str.isdigit, lines[rindex + 1][column:]))
    if numstr:
        ret[rindex + 1, column] = int(numstr)

    return ret


def process_part1(lines: list[str]) -> str:
    symbols = string.punctuation.replace(".", "")

    parts: dict[tuple[int, int], int] = dict()
    for rindex, line in enumerate(lines):
        for cindex, character in enumerate(line):
            if character in symbols:
                numbers = find_numbers(lines, rindex, cindex)
                parts |= numbers
    return str(sum(parts.values()))


def process_part2(lines: list[str]) -> str:
    sum_ = 0
    for rindex, line in enumerate(lines):
        for cindex, character in enumerate(line):
            if character == "*":
                numbers = find_numbers(lines, rindex, cindex)
                if len(numbers) == 2:
                    sum_ += prod(numbers.values())
    return str(sum_)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "4361"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "467835"
    print("testing part 2: ✓")


def solve_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-solving.txt")]
    solution = process_part1(lines)
    print(f"solving part 1: {solution}")


def solve_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-solving.txt")]
    solution = process_part2(lines)
    print(f"solving part 2: {solution}")


def main():
    test_part1()
    solve_part1()
    test_part2()
    solve_part2()


if __name__ == "__main__":
    main()
