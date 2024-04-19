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
    kmeans = KMeans(EuclideanMethod())
elif method == 2:
    kmeans = KMeans(ManhattanMethod())
else:
    print("Invalid Method number.")
    exit()

k = int(input("Enter K: "))
# k = 2

if k <= 0:
    print("Invalid K number.")

# Load points into pandas dataframe and cleaning data
df = pd.read_csv('./p1kmeans_points1.csv', names=['x', 'y', 'z'])

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
# centers_point = [Point(1, 2, 3), Point(3, 4, 5)]
kmeans.set_centers(centers_point)
kmeans.set_points(df)
kmeans.find_clusters()

while not kmeans.find_new_centers():
    kmeans.find_clusters()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
m = ['.', 'v', 's', '*', 'D', 'o', '^', 'H', '<', '>']
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
