from __future__ import annotations

import argparse
import os.path
import re

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
PAT_SYMBOL = r'(?!\.)\D'
PAT_NUM = r'\d+'
NUM_MATCHES = {}
SYM_MATCHES = {}
NUMS = {}


def compute(s: str) -> int:
    lines = s.splitlines()
    total = 0
    for index, line in enumerate(lines):
        for match in re.finditer(PAT_NUM, line):
            NUM_MATCHES[(
                index, match.span()[0], match.span()[1],
            )] = match.group()
        for match in re.finditer(PAT_SYMBOL, line):
            SYM_MATCHES[(
                index, match.span()[0], match.span()[1],
            )] = match.group()

    # count the number only if symbol is nearby
    for num_match, value in NUM_MATCHES.items():
        for sym_match, _ in SYM_MATCHES.items():
            # check in same row
            if num_match[0] == sym_match[0]:
                if (
                    num_match[1] == sym_match[2]
                    or num_match[2] == sym_match[1]
                ):
                    NUMS[num_match] = value
            # check above and below row for symbol
            if (
                num_match[0]+1 == sym_match[0]
                or num_match[0]-1 == sym_match[0]
            ):
                if len(
                    set(range(num_match[1], num_match[2]))
                    .intersection(range(sym_match[1]-1, sym_match[2]+1)),
                ) != 0:
                    NUMS[num_match] = value
    for _, v in NUMS.items():
        total += int(v)
    return total


INPUT_S = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 4361),
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
