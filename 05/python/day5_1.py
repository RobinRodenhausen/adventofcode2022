#!/usr/bin/env python3

def get_stacks(lines):
    # Get only lines until linebreak
    stack_lines = []
    for line in lines:
        if line == '\n':
            break
        stack_lines.append(line[:-1])

    # Map column index to index in string/line
    index_in_line = [i for i, char in enumerate(stack_lines[-1]) if char != ' ']

    # Strip lines of additional spaces and only get stack values
    strip_lines = []
    for index_line, value_line in enumerate(stack_lines[:-1]):
        strip_lines.append([])
        for value_string in index_in_line:
            strip_lines[index_line].append(value_line[value_string])

    stacks = []
    # Reverse order of lines to correctly fill stack
    strip_lines.reverse()

    # Turn lines into columns
    for i_column in range(len(strip_lines[0])):
        stacks.append([])
        for i_line in range(len(stack_lines)-1):
            if (strip_lines[i_line][i_column] != ' '):
                stacks[i_column].append(strip_lines[i_line][i_column])

    return stacks


def get_movements(lines):
    instructions = []
    for line in lines:
        # Ignore any non move lines
        if not line.startswith('move'):
            continue

        # Get relevant values from move instructions. Subtract 1 from source and target to match list index
        split = line.strip().split(' ')
        instructions.append({'amount': int(split[1]), 'source': int(split[3]) - 1, 'target': int(split[5]) - 1})
    return instructions


if __name__ == '__main__':
    with open('5/input', 'r') as f:
        lines = f.readlines()

    stacks = get_stacks(lines)
    movements = get_movements(lines)

    for move in movements:
        for i in range(move['amount']):
            stacks[move['target']].append(stacks[move['source']].pop())

    # Print top element of each stack
    print(''.join([s[-1] for s in stacks]))
