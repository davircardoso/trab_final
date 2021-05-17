import numpy as np
from math import exp
from numpy import linalg

e = exp(1)

h1 = np.array([1, 1, 1, 1, 1, 1])
xi = np.array([1, 2, 3, 4, 5, 6])

yt = np.array([3.7377, 4.2047, 4.7185, 5.1985, 5.7494, 6.2989])
yi = np.array([0.51,  0.65,  0.76,  0.81,  0.84,  0.92])

A = np.array([[np.dot(h1, h1), np.dot(h1, xi)], [np.dot(xi, h1), np.dot(xi, xi)]])

b = np.array(([np.dot(yi, h1)],[np.dot(yi, xi)]))

result = linalg.solve(A,b)
print(result)
c1 = result[0]
c2 = result[1]
c1 = e ** c1
print(c1)