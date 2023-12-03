#!/usr/bin/env python3

import fileinput
from math import prod

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    colors = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    possible = []
    for line in lines:
        game, subsets = line.split(": ")
        subsets = subsets.split("; ")
        is_possible = True
        for subset in subsets:
            cubes = subset.split(", ")
            for cube in cubes:
                amount, color = cube.split(" ")
                if int(amount) > colors[color]:
                    is_possible = False
        if is_possible:
            possible.append(int(game.split(" ")[1]))
    return str(sum(possible))


def process_part2(lines: list[str]) -> str:
    sum_ = 0
    for line in lines:
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        game, subsets = line.split(": ")
        subsets = subsets.split("; ")
        for subset in subsets:
            cubes = subset.split(", ")
            for cube in cubes:
                amount, color = cube.split(" ")
                colors[color] = max(colors[color], int(amount))
        sum_ += prod(colors.values())
    return str(sum_)

def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part1(lines)
    assert solution == "8"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing.txt")]
    solution = process_part2(lines)
    assert solution == "2286"
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
