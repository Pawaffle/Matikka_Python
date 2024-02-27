import numpy as np
from sympy import symbols

x, y, z = symbols('x, y, z')

# Laske edellinen tehtävä (3. 5.2.2, matriisilaskentaa)

A_matrix = np.array([[-1, 2], [3, -5]])
B_matrix = np.array([[2, 0], [-1, 4]])

print(f'A - matriisi \n{A_matrix}\n\n'
      f'B - matriisi \n{B_matrix}\n')

print(f'2A + 3B \n{2 * A_matrix + 3 * B_matrix}\n\n'
      f' A - B \n{A_matrix - B_matrix}\n')