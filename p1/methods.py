from abc import abstractmethod
from math import sqrt


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def get_z(self) -> float:
        return self.z

    def get_point(self) -> dict:
        return {'x': self.x, 'y': self.y, 'z': self.z}


class Method:

    @abstractmethod
    def distance(self, p1: Point, p2: Point) -> float:
        pass


class EuclideanMethod(Method):

    def distance(self, p1: Point, p2: Point) -> float:
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


class ManhattanMethod(Method):

    def distance(self, p1: Point, p2: Point) -> float:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)
