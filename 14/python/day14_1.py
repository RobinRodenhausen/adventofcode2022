#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def copy(self):
        return Point(self.x, self.y)

@dataclass
class RockPath:
    points: list

    def __init__(self, input_line) -> None:
        self.points = []
        split = input_line.split(' ')
        for index, point in enumerate(split):
            if index % 2 == 0:
                s = point.split(',')
                self.points.append(Point(int(s[0]), int(s[1])))

        for i in range(len(self.points)-1):
            self.points.extend(self._get_between_points(self.points[i], self.points[i+1]))
        self.points.sort()

    def _get_between_points(self, start: Point, end: Point) -> list:
        r = []
        if start.x == end.x:
            for y in range(min(start.y+1, end.y+1), max(start.y, end.y)):
                r.append(Point(start.x, y))
        elif start.y == end.y:
            for x in range(min(start.x+1, end.x+1), max(start.x, end.x)):
                r.append(Point(x, start.y))
        else:
            raise Exception('Points are diagonal to each other')
        return r

    def debug(self) -> None:
        print(self.points)

class Cave:
    def __init__(self) -> None:
        self.rockpaths = []
        self.cave = [[]]
        self.sand_total = 0

    def add_rockpath(self, rockpath: RockPath) -> None:
        self.rockpaths.append(rockpath)

    def create_cave(self):
        self.min_x = min([point.x for rockpath in self.rockpaths for point in rockpath.points])
        self.min_y = min([point.y for rockpath in self.rockpaths for point in rockpath.points])
        self.max_x = max([point.x for rockpath in self.rockpaths for point in rockpath.points]) + 1
        self.max_y = max([point.y for rockpath in self.rockpaths for point in rockpath.points]) + 1
        self.offset_x = self.min_x

        self.cave = [['.' for x in range(self.max_x - self.offset_x)] for y in range(self.max_y)]
        for rockpath in self.rockpaths:
            for point in rockpath.points:
                self.cave[point.y][point.x - self.offset_x] = '#'

        self.sand_drop_point = Point(500 - self.offset_x, 0)
        self.sand_current_position = self.sand_drop_point.copy()
        self.sand_at_rest = False
        self.sand_in_void = False

    def drop_sand(self):
        while not self.sand_in_void:
            self.sand_step()

    def sand_step(self):
        if self.sand_at_rest:
            self.cave[self.sand_current_position.y][self.sand_current_position.x] = 'o'
            self.sand_current_position = self.sand_drop_point.copy()
            self.sand_at_rest = False
            self.sand_total += 1
            self.draw_cave()

        if self.sand_current_position.y + 1 >= self.max_y:
            self.sand_in_void = True
        elif self.cave[self.sand_current_position.y + 1][self.sand_current_position.x] == '.':
            self.sand_current_position.y += 1
        elif self.sand_current_position.x - 1 < 0:
            self.sand_in_void = True
        elif self.cave[self.sand_current_position.y + 1][self.sand_current_position.x - 1] == '.':
            self.sand_current_position.y += 1
            self.sand_current_position.x -= 1
        elif self.sand_current_position.x + 1 > self.max_x:
            self.sand_in_void = True
        elif self.cave[self.sand_current_position.y + 1][self.sand_current_position.x + 1] == '.':
            self.sand_current_position.y += 1
            self.sand_current_position.x += 1
        else:
            self.sand_at_rest = True

    def get_total_sand(self) -> int:
        return self.sand_total

    def draw_cave(self):
        for line in self.cave:
            print(''.join(line))
        print('-----')

    def debug(self):
        for rp in self.rockpaths:
            rp.debug()
        print(f'Min X: {self.min_x}')
        print(f'Max X: {self.max_x}')
        print(f'Min Y: {self.min_y}')
        print(f'Max Y: {self.max_y}')

if __name__ == '__main__':
    with open('14/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    cave = Cave()
    for line in lines:
        cave.add_rockpath(RockPath(line))

    cave.create_cave()
    cave.drop_sand()
    print(cave.get_total_sand())
