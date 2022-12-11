#!/usr/bin/env python3

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

if __name__ == '__main__':
    with open('7/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    current_path = ''
    tree = {}
    for line in lines:
        if line.startswith('$ cd'):
            split = line.split(' ')
            # absolute path
            if split[2].startswith('/'):
                current_path = split[2]
            # go up
            elif split[2] == '..':
                current_path = current_path[:current_path.rindex('/')]
            # go down
            else:
                current_path += f'{split[2]}' if current_path == '/' else f'/{split[2]}'
            if not current_path in tree:
                tree[current_path] = []
        elif line[0].isdigit():
            tree[current_path].append(int(line.split(' ')[0]))

    tree_sum = {}
    # Create sum for each directory
    for key1 in tree:
        dir_total = 0
        for key2 in tree:
            if key2.startswith(key1):
                dir_total += sum(tree[key2])
        tree_sum[key1] = dir_total

    total_7_1 = 0
    required_space = REQUIRED_SPACE - (TOTAL_SPACE - tree_sum['/'])
    total_7_2 = TOTAL_SPACE

    for key in tree_sum:
        if tree_sum[key] < 100000:
            total_7_1 += tree_sum[key]
        if tree_sum[key] >= required_space and tree_sum[key] < total_7_2:
            total_7_2 = tree_sum[key]

    print(f'7.1: {total_7_1}')
    print(f'7.2: {total_7_2}')
