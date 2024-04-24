import numpy as np

A = np.array([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

B = np.array([
    54,
    12,
    6
])

X = np.linalg.inv(A).dot(B)

print('x = {0:.2f}, y = {1:.2f}, z = {2:.2f}'.format(*X))