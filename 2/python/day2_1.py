#!/usr/bin/env python3

with open('2/input', 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    input = line.strip().split(' ')

    enemy = ord(input[0]) - 64
    me = ord(input[1]) - 87

    total += me

    if enemy == me:
        total += 3
    elif me > enemy % 3 and me - enemy % 3 == 1:
        total += 6

print(f'Total: {total}')
