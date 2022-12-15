#!/usr/bin/env python3

from dataclasses import dataclass
import itertools

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
    distance: int

    def __init__(self, sensor_x, sensor_y, beacon_x, beacon_y) -> None:
        self.sensor = Point(sensor_x, sensor_y)
        self.beacon = Point(beacon_x, beacon_y)
        self.distance = abs(self.sensor.x - self.beacon.x) + abs(self.sensor.y - self.beacon.y)

    def __eq__(self, __o: object) -> bool:
        return self.sensor == __o.sensor and self.beacon == __o.beacon

    def copy(self):
        return Sensor(self.sx, self.sy, self.bx, self.by)

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

    row_y = 10
    row_y = 2000000
    row = []

    min_x = min([sensor.sensor.x - (sensor.distance - abs(sensor.sensor.y - row_y)) for sensor in sensors if not abs(row_y - sensor.sensor.y) > sensor.distance])
    max_x = max([sensor.sensor.x + (sensor.distance - abs(sensor.sensor.y - row_y)) for sensor in sensors if not abs(row_y - sensor.sensor.y) > sensor.distance])

    for i in range(min_x, max_x + 1):
        row.append(Point(i, row_y))

    no_beacon_points = []

    for point, sensor in itertools.product(row, sensors):
        # distance point on row smaller
        if abs(sensor.sensor.x - point.x) + abs(sensor.sensor.y - point.y) <= sensor.distance:
            no_beacon_points.append(point)
    # Remove duplicates
    no_beacon_points = list(dict.fromkeys(no_beacon_points))
    # Remove beacons on line
    for sensor in sensors:
        if sensor.beacon in no_beacon_points:
            no_beacon_points.remove(sensor.beacon)

    print(f'15.1: {len(no_beacon_points)}')

