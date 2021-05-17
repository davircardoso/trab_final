import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
y = np.array([1.67,  1.91,  2.15,  2.24,  2.33,  2.52, 2.78, 2.93, 3.03, 3.15, 3.19, 3.31, 3.5, 3.61])


def sistema_aumentado(x, y, dim):
    A = np.array([])
    b = np.array([])
    for i in range(0, dim + 1):
        for k in range(0, dim + 1):
            tx = np.sum(x ** (i + k))
            A = np.append(A, tx)

        ty = np.sum(y * (x ** i))

        b = np.append(b, ty)

    return A, b

def fn(x, a):
    px = 0
    for i in range(0, np.size(a)):
        px += (a[i] * (x ** i))
    return px

n = 2

A, b = sistema_aumentado(x, y, n)

A = np.reshape(A, ((n + 1), (n + 1)))
b = np.reshape(b, ((n + 1), 1))

a = np.linalg.solve(A, b)

print(a)


#plt.plot(x, y)
plt.scatter(x,y, c = 'orange')
plt.plot(x, fn(x, a))
plt.grid(True)
plt.show()

