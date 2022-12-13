#!/usr/bin/env python3

import json

class SignalPairs:
    def __init__(self, lines) -> None:
        self._parse_lines(lines)
        self.correct_order = self._check_pair_order(self.left, self.right)

    def _parse_lines(self, lines):
        if len(lines) > 2:
            raise Exception('Too many lines')
        self.left = json.loads(lines[0])
        self.right = json.loads(lines[1])

    def _check_pair_order(self, left, right) -> bool:
        if isinstance(left, int) and isinstance(right, int):
            return left < right
        elif isinstance(left, int) and isinstance(right, list):
            return self._check_pair_order([left], right)
        elif isinstance(left, list) and isinstance(right, int):
            return self._check_pair_order(left, [right])
        elif isinstance(left, list) and isinstance(right, list):
            for i in zip(left, right):
                if i[0] == i[1]:
                    continue
                return self._check_pair_order(i[0], i[1])
            return len(left) <= len(right)

    def is_correct_order(self) -> bool:
        return self.correct_order

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

    total = 0
    for index, signal in enumerate(signal_pairs, start=1):
        if signal.is_correct_order():
            total += index

    print(f'13.1: {total}')
