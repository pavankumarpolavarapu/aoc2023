from __future__ import annotations

import argparse
import os.path
import re

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    text_to_number = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "zero":"0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "0":"0",
       }
    lines = [line for line in s.splitlines()]
    first = 0
    last = 0
    temp = 0
    sum = 0
    for line in lines:
        matches = re.compile(fr'{"|".join(s for s in text_to_number)}').search(line)
        assert matches is not None
        first = text_to_number.get(matches[0])
        matches = re.compile(fr'{"|".join(s[::-1] for s in text_to_number)}').search(line[::-1])
        assert matches is not None
        last = text_to_number.get(matches[0][::-1])
        sum += int(f"{first}{last}")
    return sum
INPUT_S = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 281),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
