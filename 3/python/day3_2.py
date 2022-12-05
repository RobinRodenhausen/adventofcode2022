#!/usr/bin/env python3

from itertools import islice

with open('3/input', 'r') as f:
    total = 0
    while True:
        lines = [line.strip() for line in list(islice(f, 3))]
        if not lines:
            break

        duplicate = list(set(lines[0]).intersection(lines[1], lines[2]))[0]
        total += ord(duplicate) - 38 if duplicate.isupper() else ord(duplicate) - 96

    print(f'Total: {total}')
