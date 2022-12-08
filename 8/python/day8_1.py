#!/usr/bin/env python3

import numpy as np

tree = np.dtype([('x', int), ('y', int), ('height', int), ('visible', bool)])

def max_tree(tree_list) -> int:
    max_height = 0
    for tree in tree_list:
        if tree['height'] > max_height:
            max_height = tree['height']
    return max_height


def check_tree_line(index, tree_line) -> bool:
    if tree_line[index]['height'] > max_tree(tree_line[:index]) or tree_line[index]['height'] > max_tree(tree_line[index+1:]):
        return True
    return False


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
            forest[string_index][line_index]['visible'] = False

    for x_index, x_value in enumerate(forest):
        for y_index, y_value in enumerate(x_value):
            # Border of the forest
            if x_index == 0 or y_index == 0 or x_index == len(forest)-1 or y_index == len(x_value)-1:
                forest[x_index][y_index]['visible'] = True
            elif check_tree_line(y_index, forest[x_index]):
                forest[x_index][y_index]['visible'] = True

    forest = np.rot90(forest)

    for x_index, x_value in enumerate(forest):
        for y_index, y_value in enumerate(x_value):
            # Border of the forest
            if x_index == 0 or y_index == 0 or x_index == len(forest)-1 or y_index == len(x_value)-1:
                forest[x_index][y_index]['visible'] = True
            elif check_tree_line(y_index, forest[x_index]):
                forest[x_index][y_index]['visible'] = True

    total = 0
    for x in forest:
        for y in x:
            if y['visible']:
                total += 1

    print(total)
