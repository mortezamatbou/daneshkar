import pprint

from math import sqrt
from random import randint, choices

POINT = tuple[float, float, float]


def distance(p1: POINT, p2: POINT) -> float:
    """distance _summary_

    :param p1: _description_
    :type p1: tuple[float, float, float]
    :param p2: _description_
    :type p2: tuple[float, float, float]
    :return: _description_
    :rtype: float
    """
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def k_means(points: list[POINT], centers: list[POINT]):
    result = [
        {
            "center": center,
            "points": [],
        }
        for center in centers
    ]
    for point in points:
        index, minimum = 0, distance(point, centers[0])

        i = 1
        # for i, center in enumerate(centers):
        while i < len(centers):
            d = distance(point, centers[i])
            if d < minimum:
                index, minimum = i, d

            i += 1

        result[index]["points"].append(point)

    return result


points = [
    (9.84, -4.76, -8.57),
    (9.22, 7.58, 0.2),
    (0.68, 0.8, 1.36),
    (4.3, -0.68, -6.25),
    (-9.49, -5.19, -7.91),
    (-8.0, -1.6, 5.39),
    (5.13, -8.54, -6.69),
    (8.58, -8.13, 9.36),
    (7.27, 4.89, 6.23),
    (3.09, 1.8, 3.99),
    (-1.19, 1.06, 2.32),
    (2.09, 8.88, 4.37),
    (-4.64, 0.79, -2.26),
    (9.43, -9.89, 5.11),
    (0.14, 1.0, -4.79),
    (1.09, -4.11, 4.22),
    (4.96, -8.56, -2.65),
    (9.23, -0.61, -7.67),
    (9.12, 9.62, 0.04),
    (-2.07, 5.4, 3.92),
    (0.52, -0.09, 5.8),
    (3.59, 4.99, -0.62),
    (4.73, -5.16, 0.18),
    (6.54, 3.51, 1.25),
    (4.05, 4.27, -4.05),
    (3.91, 1.42, -8.46),
    (-3.0, -2.43, -9.9),
    (8.04, 2.95, -6.72),
    (9.35, -7.19, -8.37),
    (-9.7, -4.77, 8.37),
    (-4.67, 2.35, -3.29),
    (-4.56, 2.4, 9.44),
    (9.21, 3.56, 8.09),
    (1.92, -5.96, 9.45),
    (0.44, -8.79, -4.27),
    (-2.78, 9.33, -5.96),
    (6.57, -4.5, -3.88),
    (7.74, 2.98, 4.65),
    (-6.02, 6.25, 0.89),
    (-4.33, -0.45, -1.49),
    (-8.92, -8.1, 0.89),
    (3.54, 2.49, -7.09),
    (-6.5, 9.77, -3.37),
    (-4.92, 8.66, 4.18),
    (-2.54, -1.14, 3.29),
    (-2.9, 0.63, 5.35),
    (-9.8, -2.69, -5.38),
    (6.13, 5.35, -9.66),
    (4.32, 2.77, -2.76),
    (-4.87, 3.61, 0.21),
    (-8.63, 7.06, -7.89),
    (-9.36, 8.22, 0.89),
    (-2.45, 0.05, -6.25),
    (-2.4, 5.58, 2.57),
    (-0.25, -0.92, 5.51),
    (-8.62, 8.46, -4.76),
    (-5.49, -8.81, -2.39),
    (7.77, -9.13, -4.28),
    (4.96, -6.27, -7.33),
    (-8.53, 3.78, -7.14),
    (0.39, 5.1, -8.3),
    (-3.27, -0.72, -6.44),
    (1.32, 9.55, 4.58),
    (8.91, -8.68, 1.88),
    (-1.38, 5.13, -2.54),
    (6.66, 5.62, 8.78),
    (7.79, 3.86, 6.01),
    (9.16, -3.0, -1.79),
    (-3.23, -9.2, -4.9),
    (2.87, -3.04, -3.46),
    (9.28, -3.03, 6.34),
    (9.65, -6.92, -0.26),
    (-6.06, 8.06, -5.26),
    (9.06, 1.78, -9.04),
    (-0.78, -8.9, 6.64),
    (-7.36, -2.39, -8.25),
    (-5.09, 8.22, 2.0),
    (4.2, 1.01, -2.44),
    (7.7, 4.6, -7.96),
    (0.81, -8.31, 9.04),
    (9.59, -5.98, -4.92),
    (-9.83, -8.3, -5.09),
    (-7.65, 4.76, -6.71),
    (-1.11, -0.52, -5.27),
]

k = int(input("K = "))
centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(k)]
centers = [(1, 2, 3), (4, 5, 6)]
while True:
    clusters = k_means(points, centers)
    new_centers = []
    for cluster in clusters:
        x, y, z = zip(*cluster["points"])
        new_centers.append(
            (
                sum(x) / len(x),
                sum(y) / len(y),
                sum(z) / len(z),
            )
        )

    if new_centers == centers:
        break

    centers = new_centers

print(centers)
