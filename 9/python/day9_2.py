#!/usr/bin/env python3

from day9_1 import Coords

class Bridge:
    visited_coords_tail = []
    head = Coords(0, 0)
    tail = [Coords(0, 0) for i in range(9)]

    def __init__(self) -> None:
        for i in range(len(self.tail)):
            self.visited_coords_tail.append(self.tail[i].copy())

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

            if self._check_tail_move(self.head, self.tail[0]):
                self._move_tail(self.head, self.tail[0])
                for i in range(len(self.tail)-1):
                    if self._check_tail_move(self.tail[i], self.tail[i+1]):
                        self._move_tail(self.tail[i], self.tail[i+1])
                self.visited_coords_tail.append(self.tail[-1].copy())

    def _move_tail(self, head, tail):
        if head.x > tail.x:
            tail.x += 1
        if head.y > tail.y:
            tail.y += 1

        if head.x < tail.x:
            tail.x -= 1
        if head.y < tail.y:
            tail.y -= 1

    def _check_tail_move(self, head, tail) -> bool:
        if abs(head.x - tail.x) > 1:
            return True
        if abs(head.y - tail.y) > 1:
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
