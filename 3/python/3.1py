#!/usr/bin/env python3

with open('3/input', 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    first = line[:len(line)//2]
    second = line[len(line)//2:]

    duplicate = list(set(first).intersection(second))[0]
    total += ord(duplicate) - 38 if duplicate.isupper() else ord(duplicate) - 96

print(f'Total: {total}')
