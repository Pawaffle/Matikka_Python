from sympy import symbols, solve

x, y, z = symbols('x, y, z')

# Ratkaise tehtäväosa (1. Kertausta) kolme ensimmäistä kertaustehtävää

A1 = solve([5 * x + 3 * y - 9,
            2 * x + y - 4], [x, y, z])

A2 = solve([2 * x + y + z - 6, x + 3 * y + z - 2, 2 * x + y + 2 * z - 9], [x, y, z])

A3 = solve([x + y + 3 * z + 1, 3 * x + y + z - 5, 2 * x + y + 2 * z - 2], [x, y, z])

print("T. 1.(Yhtälöryhmät).")
print(f"a) == {A1}\n")
print(f"b) == {A2}\n")
print(f"c) == {A3}\n")