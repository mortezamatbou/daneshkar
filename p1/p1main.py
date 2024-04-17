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
    def calculate(self, p1: Point, p2: Point) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Distance:

    def __init__(self, strategy: Method):
        self.method = strategy

    def calculate(self, p1: Point, p2: Point) -> float:
        return self.method.calculate(p1, p2)

    def name(self) -> str:
        return self.method.name()


class EuclideanMethod(Method):

    def calculate(self, p1: Point, p2: Point) -> float:
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)

    def name(self) -> str:
        return "Euclidean"


class ManhattanMethod(Method):

    def calculate(self, p1: Point, p2: Point) -> float:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)

    def name(self) -> str:
        return "Manhattan"


print("Select method of calculate")
print("1) Euclidean\n2) Manhattan")

method = int(input("Enter num of method: "))

if method == 1:
    distance = Distance(EuclideanMethod())
elif method == 2:
    distance = Distance(ManhattanMethod())
else:
    print("Invalid Method number.")
    exit()

k = int(input("Enter K: "))

if k <= 0:
    print("Invalid K number.")

print("Calculate method:", distance.name())
print("K={}".format(k))

p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

d = distance.calculate(p1, p2)
print(d)
