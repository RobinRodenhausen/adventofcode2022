#!/usr/bin/env python3

with open('1/input', 'r') as f:
    lines = f.readlines()

total, calories = 0, []

for line in lines:
    if line == '\n':
        calories.append(total)
        total = 0
    else:
        total += int(line.strip())

calories.sort()
print(f'1.1: {calories[-1]}')
print(f'1.2: {sum(calories[-3:])}')
