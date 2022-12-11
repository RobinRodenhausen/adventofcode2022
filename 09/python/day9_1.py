#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Coords:
    x: int = -1
    y: int = -1

    def copy(self):
        return Coords(self.x, self.y)

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash(('x', self.x, 'y', self.y))

class Bridge:
    visited_coords_tail = []
    head = Coords(0, 0)
    tail = Coords(0, 0)

    def __init__(self) -> None:
        self.visited_coords_tail.append(self.tail.copy())

    def move(self, direction, steps):
        for i in range(steps):
            match direction:
                case 'R':
                    self.head.x += 1
                case 'L':
                    self.head.x -= 1
                case 'U':
                    self.head.y += 1
                case 'D':
                    self.head.y -= 1

            if self._check_tail_move():
                self._move_tail()

    def _move_tail(self):
        if self.head.x > self.tail.x:
            self.tail.x += 1
        if self.head.y > self.tail.y:
            self.tail.y += 1

        if self.head.x < self.tail.x:
            self.tail.x -= 1
        if self.head.y < self.tail.y:
            self.tail.y -= 1

        self.visited_coords_tail.append(self.tail.copy())

    def _check_tail_move(self) -> bool:
        if abs(self.head.x - self.tail.x) > 1:
            return True
        if abs(self.head.y - self.tail.y) > 1:
            return True
        return False

    def get_total_visited_tail(self) -> int:
        return len(list(set(self.visited_coords_tail)))


if __name__ == '__main__':
    with open('9/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    bridge = Bridge()
    for line in lines:
        split = line.split(' ')
        bridge.move(direction=split[0], steps=int(split[1]))

    print(bridge.get_total_visited_tail())
