#!/usr/bin/env python3

import numpy as np

tree = np.dtype([('x', int), ('y', int), ('height', int), ('view', int)])

def block_view(height, tree_list) -> int:
    total_view = 0
    for tree in tree_list:
        if height > tree['height']:
            total_view += 1
        else:
            total_view += 1
            break

    return total_view

def check_tree_line(index, tree_line) -> None:
    tree_line[index]['view'] *= block_view(tree_line[index]['height'], tree_line[index+1:])
    tree_line[index]['view'] *= block_view(tree_line[index]['height'], tree_line[:index][::-1])


if __name__ == '__main__':
    with open('8/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    forest = np.empty(shape=[len(lines), len(lines[0])], dtype=tree)

    for line_index, line in enumerate(lines):
        for string_index, string in enumerate(line):
            forest[string_index][line_index]['x'] = string_index
            forest[string_index][line_index]['y'] = line_index
            forest[string_index][line_index]['height'] = int(string)
            forest[string_index][line_index]['view'] = 1


    for x_index, x_value in enumerate(forest):
        for y_index, y_value in enumerate(x_value):
            if x_index == 0 or y_index == 0 or x_index == len(forest)-1 or y_index == len(x_value)-1:
                forest[x_index][y_index]['view'] = 0
            else:
                check_tree_line(y_index, forest[x_index])

    forest = np.rot90(forest)

    for x_index, x_value in enumerate(forest):
        for y_index, y_value in enumerate(x_value):
            if x_index == 0 or y_index == 0 or x_index == len(forest)-1 or y_index == len(x_value)-1:
                forest[x_index][y_index]['view'] = 0
            else:
                check_tree_line(y_index, forest[x_index])

    max = 0
    for x in forest:
        for y in x:
            if y['view'] > max:
                max = y['view']

    print(max)
