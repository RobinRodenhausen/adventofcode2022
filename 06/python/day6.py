#!/usr/bin/env python3

START_MARKER = 4
MESSAGE_MARKER = 14

def get_marker(line, marker_length):
    for index, _ in enumerate(line):
        if len(dict.fromkeys(line[index:index + marker_length])) == marker_length:
            return index + marker_length


if __name__ == '__main__':
    with open('6/input', 'r') as f:
        lines = f.readlines()

    print(f'6.1: {get_marker(lines[0], START_MARKER)}')
    print(f'6.1: {get_marker(lines[0], MESSAGE_MARKER)}')
