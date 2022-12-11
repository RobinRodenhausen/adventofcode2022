#!/usr/bin/env python3

with open('4/input', 'r') as f:
    lines = f.readlines()

total_4_1 = 0
total_4_2 = 0

for line in lines:
    pair = line.strip().split(',')
    p1 = pair[0].split('-')
    p2 = pair[1].split('-')
    p1_range = set(range(int(p1[0]), int(p1[1]) + 1))
    p2_range = set(range(int(p2[0]), int(p2[1]) + 1))

    if p1_range.issubset(p2_range) or p2_range.issubset(p1_range):
        total_4_1 += 1
    if p1_range.intersection(p2_range):
        total_4_2 += 1

print(f'Total 4.1: {total_4_1}')
print(f'Total 4.2: {total_4_2}')
