#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class CPU:
    cycle: int
    register: int

    def __init__(self, cycle, register) -> None:
        self.cycle = cycle
        self.register = register

if __name__ == '__main__':
    with open('10/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    register = 1
    cycle = 0
    cycles = []

    for line in lines:
        cycle += 1
        cycles.append(CPU(cycle, register))

        if line.startswith('noop'):
            continue
        if line.startswith('addx'):
            cycle += 1
            cycles.append(CPU(cycle, register))
            register += int(line.split(' ')[1])

    total = 0
    screen = [[' ' for x in range(40)] for y in range(6)]

    for cycle in cycles:
        if cycle.cycle % 40 == 20:
            total += cycle.cycle * cycle.register

        crt_line = (cycle.cycle - 1) // 40
        pixel = (cycle.cycle - 1) % 40
        sprite_position = range(cycle.register - 1, cycle.register + 2)
        if pixel in sprite_position:
            screen[crt_line][pixel] = '#'
        else:
            screen[crt_line][pixel] = '.'

    print(f'10.1: {total}')
    print('10.2:')
    for line in screen:
        print(''.join(line))
