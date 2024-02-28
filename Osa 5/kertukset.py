import numpy as np

# a
A1 = np.array([
        [-1, 2],
        [3, 1]
    ])

A2 = np.array([
        [0, 1, 3],
        [2, -3, 5]
])

print(f'a)\n  {np.dot(A1, A2)}\n')

# b
B1 = np.array([
        [1, 3, 5],
        [0, -2, 1],
        [2, -1, 4]
    ])

B2 = np.array([
        [1],
        [-3],
        [-1]
])

print(f'b)\n  {np.dot(B1, B2)}\n')

# c
C1 = np.array([
        [2, 0, 1],
        [1, -3, 4],
        [0, 1, 5]
    ])

C2 = np.array([
        [3],
        [-5],
        [7]
])

print(f'c)\n  {np.dot(C1, C2)}\n')

# d
D1 = np.array([
        [1, -4, 2],
        [3, 0, -2],
        [2, 1, 0]
    ])

D2 = np.array([
        [5, 1, -1],
        [-2, 1, 3],
        [0, 3, 4]
])

print(f'd)\n  {np.dot(D1, D2)}\n')

