#!/usr/bin/env python3

import json
import functools

def check_pair_order(left, right) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, int) and isinstance(right, list):
        return check_pair_order([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return check_pair_order(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for i in zip(left, right):
            if i[0] == i[1]:
                continue
            return check_pair_order(i[0], i[1])
        return len(left) - len(right)

class SignalPairs:
    def __init__(self, lines) -> None:
        self._parse_lines(lines)
        self.correct_order = check_pair_order(self.left, self.right)

    def _parse_lines(self, lines):
        if len(lines) > 2:
            raise Exception('Too many lines')
        self.left = json.loads(lines[0])
        self.right = json.loads(lines[1])

    def is_correct_order(self) -> bool:
        return self.correct_order

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def debug(self) -> None:
        print(self.left)
        print(self.right)
        print(self.correct_order)


if __name__ == '__main__':
    with open('13/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    signal_pairs = []
    signal_lines = []
    for line in lines:
        signal_lines.append(line)
        if not line or line == lines[-1]:
            signal_pairs.append(SignalPairs(signal_lines[:2]))
            signal_lines.clear()

    MARKER_1 = [[2]]
    MARKER_2 = [[6]]
    signals = []
    signals.append(MARKER_1)
    signals.append(MARKER_2)
    for signal in signal_pairs:
        signals.append(signal.get_left())
        signals.append(signal.get_right())

    signals = sorted(signals, key=functools.cmp_to_key(check_pair_order))

    print(f'13.2: {(signals.index(MARKER_1)+1) * (signals.index(MARKER_2)+1)}')
