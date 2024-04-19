import random

f = open("p1kmeans_points3.csv", "w")
lines = ''
for i in range(3000):
    line = '{},{},{}'.format(round(random.uniform(-10, 10), 2), round(random.uniform(-10, 10), 2),
                             round(random.uniform(-10, 10), 2))

    lines += line + "\n"

f.write(lines)
f.close()
