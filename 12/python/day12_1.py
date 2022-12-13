#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Coord:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def copy(self):
        return Coord(self.x, self.y)

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash(('x', self.x, 'y', self.y))

class Elevation:
    def __init__(self, lines) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        self.elevation_map = [[-1 for x in range(self.x_size)] for y in range(self.y_size)]

        for l_index, line in enumerate(lines):
            for c_index, char in enumerate(line):
                if char == 'S':
                    self.start = Coord(c_index, l_index)
                    char = 'a'
                elif char == 'E':
                    self.end = Coord(c_index, l_index)
                    char = 'z'
                self.elevation_map[l_index][c_index] = ord(char) - 97

        self.total_steps = 0
        self.possible_locations = [[self.start]]

    def check_right(self, coord: Coord):
        if coord.x < self.x_size - 1:
            if self.elevation_map[coord.y][coord.x] + 1 >= self.elevation_map[coord.y][coord.x + 1]:
                return True
        return False

    def check_left(self, coord: Coord):
        if coord.x > 0:
            if self.elevation_map[coord.y][coord.x] + 1 >= self.elevation_map[coord.y][coord.x - 1]:
                return True
        return False

    def check_down(self, coord: Coord):
        if coord.y < self.y_size - 1:
            if self.elevation_map[coord.y][coord.x] + 1 >= self.elevation_map[coord.y + 1][coord.x]:
                return True
        return False

    def check_up(self, coord: Coord):
        if coord.y > 0:
            if self.elevation_map[coord.y][coord.x] + 1 >= self.elevation_map[coord.y - 1][coord.x]:
                return True
        return False

    def step(self):
        self.total_steps += 1
        print(f'Step {self.total_steps}')
        self.possible_locations.append([])
        for coord in self.possible_locations[self.total_steps - 1]:
            if self.check_right(coord):
                new = Coord(coord.x + 1, coord.y)
                if not self.check_already_visited(new):
                    self.possible_locations[self.total_steps].append(new)
            if self.check_left(coord):
                new = Coord(coord.x - 1, coord.y)
                if not self.check_already_visited(new):
                    self.possible_locations[self.total_steps].append(new)
            if self.check_up(coord):
                new = Coord(coord.x, coord.y - 1)
                if not self.check_already_visited(new):
                    self.possible_locations[self.total_steps].append(new)
            if self.check_down(coord):
                new = Coord(coord.x, coord.y + 1)
                if not self.check_already_visited(new):
                    self.possible_locations[self.total_steps].append(new)

    def check_already_visited(self, check_loc):
        for locations in self.possible_locations:
            if check_loc in locations:
                return True
        return False

    def get_shortest_step(self):
        while not self.end in self.possible_locations[self.total_steps]:
            #print(f'Ok {i} TS: {self.total_steps}')
            #print(self.possible_locations[self.total_steps])
            #print(self.end)
            self.step()
        return self.total_steps


if __name__ == '__main__':
    with open('12/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    e = Elevation(lines)
    print(e.get_shortest_step())
