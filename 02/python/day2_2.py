#!/usr/bin/env python3

with open('2/input', 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    input = line.strip().split(' ')

    enemy = ord(input[0]) - 64
    result = (ord(input[1]) - 88) * 3

    total += result

    match result:
        case 0:
            total += 3 if enemy == 1 else (enemy - 1)
        case 3:
            total += enemy
        case 6:
            total += (enemy % 3) + 1

print(f'Total: {total}')
