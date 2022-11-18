def bernsley_fern(iterations, f1, f2, f3, f4, x, y):

    current = 0

    for i in range(1, iterations):

        z = randint(1, 100)

        if z == 1:
            x.append(f1[0][0]*(x[current]) + f1[0][1]*(y[current]) + f1[0][2])
            y.append(f1[1][0]*(x[current]) + f1[1][1]*(y[current]) + f1[1][2])

        if z >= 2 and z <= 86:
            x.append(f2[0][0]*(x[current]) + f2[0][1]*(y[current]) + f2[0][2])
            y.append(f2[1][0]*(x[current]) + f2[1][1]*(y[current]) + f2[1][2])

        if z >= 87 and z <= 93:
            x.append(f3[0][0]*(x[current]) + f3[0][1]*(y[current]) + f3[0][2])
            y.append(f3[1][0]*(x[current]) + f3[1][1]*(y[current]) + f3[1][2])

        if z >= 94 and z <= 100:
            x.append(f4[0][0]*(x[current]) + f4[0][1]*(y[current]) + f4[0][2])
            y.append(f4[1][0]*(x[current]) + f4[1][1]*(y[current]) + f4[1][2])

        current = current + 1

    return x, y

import matplotlib.pyplot as plt
from random import randint

iterations = 50000
# f1 = [[0, 0, 0], [0, 0.16, 0]]
# f2 = [[0.85, 0.04, 0], [-0.04, 0.85, 1.6]]
# f3 = [[0.2, -0.26, 0], [0.23, 0.22, 1.6]]
# f4 = [[-0.15, 0.28, 0], [0.26, 0.24, 0.44]]
f1 = [[0, 0, 0], [0, 0.16, 0]]
f2 = [[0.85, 0.04, 0], [-0.04, 0.85, 1.6]]
f3 = [[0.2, -0.26, 0], [0.23, 0.22, 1.6]]
f4 = [[-0.15, 0.28, 0], [0.26, 0.24, 0.44]]

x, y = [0], [0]
x, y = bernsley_fern(iterations, f1, f2, f3, f4, x, y)

plt.scatter(x, y, s=0.2, edgecolor='green')
plt.show()
