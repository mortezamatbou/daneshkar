import random
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
from p1.cluster import KMeans
from p1.methods import EuclideanMethod, ManhattanMethod, Point

print("Select method of calculate")
print("1) Euclidean\n2) Manhattan")

method = int(input("Enter num of method: "))
# method = 1

if method == 1:
    method_name = 'Euclidean Distance'
    kmeans = KMeans(EuclideanMethod())
elif method == 2:
    method_name = 'Manhattan Distance'
    kmeans = KMeans(ManhattanMethod())
else:
    print("Invalid Method number.")
    exit()

k = int(input("Enter K: "))
# k = 2

if k <= 0:
    print("Invalid K number.")

fig = plt.figure(figsize=plt.figaspect(0.5))
fig.suptitle("{} k={}".format(method_name, k))

maps = [
    {'id': 'ax1', 'file': './p1kmeans_points1.csv'},
    # {'id': 'ax2', 'file': './p1kmeans_points2.csv'},
    {'id': 'ax3', 'file': './p1kmeans_points3.csv'}
]
files = [
    './p1kmeans_points1.csv',
    './p1kmeans_points2.csv',
    './p1kmeans_points3.csv'
]

for idx, f in enumerate(files):
    # Load points into pandas dataframe and cleaning data
    df = pd.read_csv(f, names=['x', 'y', 'z'])

    for i in df.index:
        try:
            float(df.loc[i, 'x'])
            float(df.loc[i, 'y'])
            float(df.loc[i, 'z'])
        except:
            df.drop(i, inplace=True)

    df.dropna(inplace=True)
    df = df.astype(float)

    centers_point = [Point(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(k)]
    kmeans.set_centers(centers_point)
    kmeans.set_points(df)
    kmeans.find_clusters()

    while not kmeans.find_new_centers():
        kmeans.find_clusters()

    m = ['.', 'v', 's', '*', 'D', 'o', '^', 'H', '<', '>']
    ax = fig.add_subplot(1, len(files), idx + 1, projection='3d')
    ax.set_title(f)

    for cluster in kmeans.clusters:
        x = list(cluster['points']['x'])
        y = list(cluster['points']['y'])
        z = list(cluster['points']['z'])
        random.shuffle(m)
        ax.scatter(x, y, z, marker=m.pop())

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

plt.show()
