#!/usr/bin/env python3

import fileinput

from rich import print
from rich.traceback import install

install(show_locals=True)


def process_part1(lines: list[str]) -> str:
    sum_ = 0
    for line in lines:
        digits = [character for character in line if str.isdigit(character)]
        calibration_value = int(digits[0] + digits[-1])
        sum_ += int(calibration_value)
    return str(sum_)


def process_part2(lines: list[str]) -> str:
    words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    sum_ = 0
    for line in lines:
        digits: list[str] = []
        for index, character in enumerate(line):
            if str.isdigit(character):
                digits.append(character)
            else:
                for word, digit in words.items():
                    if line[index:].startswith(word):
                        digits.append(digit)
        calibration_value = int(digits[0] + digits[-1])
        sum_ += int(calibration_value)
    return str(sum_)


def test_part1():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing-1.txt")]
    solution = process_part1(lines)
    assert solution == "142"
    print("testing part 1: ✓")


def test_part2():
    lines = [line.rstrip("\n") for line in fileinput.input("input-testing-2.txt")]
    solution = process_part2(lines)
    assert solution == "281"
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
