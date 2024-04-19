import pandas as pd

from .methods import Method, Point


class KMeans:

    def __init__(self, strategy: Method):
        self.method = strategy
        self.points: pd.DataFrame = pd.DataFrame([])
        self.centers: list[Point] = []
        self.clusters: list[dict["center": list[Point], "points": pd.DataFrame]] = []

    def set_centers(self, centers: list[Point]):
        self.centers = centers

    def set_points(self, points: pd.DataFrame):
        self.points = points
        return self

    def distance(self, p1: Point, p2: Point) -> float:
        return self.method.distance(p1, p2)

    def find_clusters(self) -> None:
        self.clusters = [
            {
                "center": center,
                "points": pd.DataFrame({}, columns=['x', 'y', 'z']),
            }
            for center in self.centers
        ]

        for pid, row in self.points.iterrows():
            point = Point(row['x'], row['y'], row['z'])
            index, minimum = 0, self.distance(point, self.centers[0])

            i = 1
            while i < len(self.centers):
                d = self.distance(point, self.centers[i])
                if d < minimum:
                    index, minimum = i, d
                i += 1

            self.clusters[index]['points'].loc[
                len(self.clusters[index]['points']), self.clusters[index]['points'].columns] = point.x, point.y, point.z

    def find_new_centers(self):
        new_centers = []

        for cluster in self.clusters:
            rows = len(cluster['points'])
            x = cluster['points']['x'].sum() / rows
            y = cluster['points']['y'].sum() / rows
            z = cluster['points']['z'].sum() / rows
            new_centers.append(Point(x, y, z))

        all_same = True
        for i, previous_center in enumerate(self.centers):

            if previous_center.x != new_centers[i].x or previous_center.y != new_centers[i].y or previous_center.z != \
                    new_centers[i].z:
                all_same = False

        self.centers = new_centers
        return all_same

    def get_clusters(self) -> list:
        return self.clusters
