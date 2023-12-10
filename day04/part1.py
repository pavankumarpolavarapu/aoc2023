from __future__ import annotations

import argparse
import os.path
import re

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
PAT_NUM = r'\d+'


def compute(s: str) -> int:
    lines = s.splitlines()
    winning = set()
    mine = set()
    parts = []
    points = 0
    matched = 0
    for line in lines:
        parts = line.split(':')[1].split('|')
        winning = {int(x.group()) for x in re.finditer(PAT_NUM, parts[0])}
        mine = {int(x.group()) for x in re.finditer(PAT_NUM, parts[1])}
        matched = len(winning.intersection(mine))
        if matched != 0:
            points += 2 ** (matched - 1)
    return points


INPUT_S = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 13),
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
