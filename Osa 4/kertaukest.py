from sympy import symbols, solve
x, y, z = symbols('x, y, z')

print('Osa 2 tehtävät')

A1 = solve([
            x - 2*y - 2*z,
            -2*x + y - z + 3,
            3*x + 2*y + z - 4],       [x, y, z])

B1 = solve([x + y - 1,
            2*x + y - z - 1,
            3*x + y - 2*z - 1],       [x, y, z])

A2 = solve([2*x + 4*y - z - 11,
            6*x - y - 3*z - 7,
            4*x + 5*y - 2*z - 16],       [x, y, z])

B2 = solve([4*x + 2*y - 2*z,
            2*x + y - z - 1,
            3*x + y - 2*z - 1],       [x, y, z])

print(f"1a) == {A1}\n")
print(f"1b) == {B1}\n")
print(f"2a) == {A2}\n")
print(f"2b) == {B2}\n")

print('Osa 3 tehtävät')

A1 = solve([5*x + 3*y - 9,
            2*x + y - 4], [x, y, z])

A2 = solve([2*x + y + z - 6,
            x + 3*y + z - 2,
            2*x + y + 2*z - 9], [x, y, z])

A3 = solve([x + y + 3*z + 1,
            3*x + y + z - 5,
            2*x + y + 2*z - 2], [x, y, z])

print(f"a) == {A1}\n")
print(f"b) == {A2}\n")
print(f"c) == {A3}\n")

