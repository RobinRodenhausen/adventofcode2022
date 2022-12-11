#!/usr/bin/env python3

import operator
import math

class Monkey:
    def __init__(self, lines) -> None:
        self.parse_from_lines(lines)
        self.total_inspected = 0

    def parse_from_lines(self, lines: list) -> None:
        for line in lines:
            if line.startswith('Starting items: '):
                items = line.split(':')[1].split(',')
                self.items = [int(item.strip()) for item in items]
            elif line.startswith('Operation: new = old '):
                s = line.split(' ')
                match s[-2]:
                    case '+':
                        self.op_func = operator.add
                    case '*':
                        self.op_func = operator.mul
                if s[-1] != 'old':
                    self.op_value = int(s[-1])
                else:
                    self.op_value = 0
            elif line.startswith('Test: divisible by '):
                self.test_dividend = int(line.split(' ')[-1])
            elif line.startswith('If true: throw to monkey '):
                self.test_successful_target = int(line.split(' ')[-1])
            elif line.startswith('If false: throw to monkey '):
                self.test_fail_target = int(line.split(' ')[-1])

    def inspection(self, keep_number_small) -> None:
        for index, item in enumerate(self.items):
            self.total_inspected += 1
            item = self.op_func(item, self.op_value if self.op_value else item)
            self.items[index] = item % keep_number_small

    def add_item(self, item) -> None:
        self.items.append(item)

    def get_dividend(self):
        return self.test_dividend

    def test_and_throw(self, monkeys: list) -> None:
        for item in self.items:
            if item % self.test_dividend == 0:
                monkeys[self.test_successful_target].add_item(item)
            else:
                monkeys[self.test_fail_target].add_item(item)
        self.items.clear()

    def get_total_inspected(self) -> int:
        return self.total_inspected

    # Just debug
    def print(self):
        print(f'Items: {self.items}')
        print(f'''Operation: old {self.op_func} {self.op_value if self.op_value else 'old'}''')
        print(f'Test: {self.test_dividend}')
        print(f'Test positive: {self.test_successful_target}')
        print(f'Test negativ: {self.test_fail_target}')


if __name__ == '__main__':
    with open('11/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    monkeys = []
    monkey_lines = []
    for line in lines:
        monkey_lines.append(line)
        if not line or line == lines[-1]:
            monkeys.append(Monkey(monkey_lines))
            monkey_lines.clear()

    # Alternative that can potentially result in a smaller number
    # keep_number_small = math.lcm(*[monkey.get_dividend() for monkey in monkeys])
    keep_number_small = 1
    for monkey in monkeys:
        keep_number_small *= monkey.get_dividend()

    for i in range(10000):
        for monkey in monkeys:
            monkey.inspection(keep_number_small)
            monkey.test_and_throw(monkeys)

    total_inspected = []
    for monkey in monkeys:
        total_inspected.append(monkey.get_total_inspected())

    total_inspected.sort()
    print(f'11.2: {total_inspected[-1] * total_inspected[-2]}')
