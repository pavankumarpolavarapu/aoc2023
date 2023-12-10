from __future__ import annotations

import argparse
import os.path
import re

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    PAT_RED = r'(\d+)(?=\sred)'
    PAT_GREEN = r'(\d+)(?=\sgreen)'
    PAT_BLUE = r'(\d+)(?=\sblue)'
    lines = s.splitlines()
    puzzle = []
    red = 0
    green = 0
    blue = 0
    for line in lines:
        red = max(
            (
                int(x.group())
                for x in re.finditer(PAT_RED, line)
            ), default=0,
        )
        green = max(
            (
                int(x.group())
                for x in re.finditer(PAT_GREEN, line)
            ), default=0,
        )
        blue = max(
            (
                int(x.group())
                for x in re.finditer(PAT_BLUE, line)
            ), default=0,
        )
        puzzle.append(red*green*blue)
    return sum(puzzle)


INPUT_S = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 2286),
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
