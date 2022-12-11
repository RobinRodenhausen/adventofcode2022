#!/usr/bin/env python3

from day5_1 import get_movements, get_stacks

if __name__ == '__main__':
    with open('5/input', 'r') as f:
        lines = f.readlines()

    stacks = get_stacks(lines)
    movements = get_movements(lines)

    for move in movements:
        stacks[move['target']].extend(stacks[move['source']][-move['amount']:])
        del stacks[move['source']][-move['amount']:]

    # Print top element of each stack
    print(''.join([s[-1] for s in stacks]))
