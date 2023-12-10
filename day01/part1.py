from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(s: str) -> int:
    lines = [str(line) for line in s.splitlines()]
    numbers = []
    sum = 0
    for line in lines:
        numbers = [ n for n in line if n.isdigit()]
        sum += int(numbers[-1]) + 10*int(numbers[0])
    return sum


INPUT_S = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 142),
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
