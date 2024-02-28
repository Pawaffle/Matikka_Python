import numpy as np

Ex3 = np.array([
        [-2, 0, 8, 5],
        [3, -1, 2, 1],
        [4, 7, 6, 2],
        [1, 0, 2, 3]
])

print(Ex3, '\n\n tämän matrisin determenanti on ', round(np.linalg.det(Ex3)))