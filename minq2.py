import numpy as np
import matplotlib.pyplot as plt

#x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
#y = np.array([1.67, 1.91, 2.15, 2.24, 2.33, 2.52, 2.78, 2.93, 3.03, 3.15, 3.19, 3.31, 3.5, 3.61])

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

y = np.array([22.91, 9.56, 5.22, 1.65, 8.94, 5.97, 7.67, 12.53, 9.30, 7.60, 5.69, 3.14, 4.46, 5.90, 4.31, 5.91, 6.50,
              5.84, 6.41, 10.67, 6.29, 2.95, 3.75, 4.31, 4.52])


def sistema(x, y, dim):
    m = len(x)
    A = np.empty((dim, dim))
    soma = []
    for i in range(0, dim + 4):
        aux = 0
        for k in range(0, m):
            aux = aux + x[k] ** i
        soma.append(aux)

    for i in range(0, dim):
        for j in range(i, dim):
            A[i, j] = soma[i + j]
            if (i != j):
                A[j, i] = A[i, j]

    b = []
    for i in range(0, dim):
        aux = 0
        for k in range(0, m):
            aux = aux + y[k] * (x[k] ** (i))
        b.append(aux)

    return A, b


def fn(x, a):
    px = 0
    for i in range(0, np.size(a)):
        px += (a[i] * (x ** i))
    return px


A, b = sistema(x, y, 5)


print("A = ", A)
print("b = ", b)

coef = np.linalg.solve(A, b)
print("coef = ", coef)



plt.xlabel("taxa de inflação(%)")
plt.ylabel("tempo(anos)")
plt.scatter(x, y)
plt.grid(True)
p, = plt.plot(x, fn(x, coef), c = "r")
f, = plt.plot(x, y, linestyle = 'dashed')
plt.legend((f,p),("Taxa de inflação", "Curva polinômio de quarto grau"))
plt.show()
