#!/usr/bin/env python3

from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash(('x', self.x, 'y', self.y))

    def copy(self):
        return Point(self.x, self.y)

@dataclass
class Sensor:
    sensor: Point
    beacon: Point
    radius: int

    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y) -> None:
        self.sensor = Point(sensor_x, sensor_y)
        self.beacon = Point(beacon_x, beacon_y)
        self.radius = abs(self.sensor.x - self.beacon.x) + abs(self.sensor.y - self.beacon.y)

    def __eq__(self, __o: object) -> bool:
        return self.sensor == __o.sensor and self.beacon == __o.beacon

    def copy(self):
        return Sensor(self.sx, self.sy, self.bx, self.by)

    def point_in_sensor_range(self, point: Point) -> bool:
        return abs(self.sensor.x - point.x) + abs(self.sensor.y - point.y) <= self.radius

if __name__ == '__main__':
    with open('15/input', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    sensors = []
    for line in lines:
        split = line.split(' ')
        sensor_x = int(split[2][split[2].find('=')+1:-1])
        sensor_y = int(split[3][split[3].find('=')+1:-1])
        beacon_x = int(split[8][split[8].find('=')+1:-1])
        beacon_y = int(split[9][split[9].find('=')+1:])
        sensors.append(Sensor(sensor_x, sensor_y, beacon_x, beacon_y))

    area_side = 4000000
    # area_side = 20 + 1

    def dist(x, y): return abs(x.x - y.x) + abs(x.y - y.y)

    for y in range(area_side + 1):
        ranges = defaultdict(int)
        for sensor in sensors:
            possible_x_distance = sensor.radius - abs(sensor.sensor.y - y)
            # If sensor does not reach y coordinate, skip
            if possible_x_distance < 0:
                continue
            # x limit left, 0 if start would be outside of relevant area (0 -> 4000001)
            left = max(0, sensor.sensor.x - possible_x_distance)
            # x limit right, limit (4000001) if end would be outside of relevant area (0 -> 4000001)
            right = min(area_side, sensor.sensor.x + possible_x_distance)
            # range opened at index left
            ranges[left] += 1
            # range closed at index right
            ranges[right+1] -= 1
            opened_ranges = 0
        for x in sorted(ranges.keys()):
            opened_ranges += ranges[x]
            # same amount of ranges opened and closed but not at the end of line -> gap where beacon must be
            if opened_ranges == 0 and x != area_side + 1:
                print(x, y)
                print(f'15.2: {x * 4000000 + y}')
