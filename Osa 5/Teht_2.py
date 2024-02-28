import sympy as sp
x = sp.symbols('x')

dict = {

    'Ex 1a': sp.Matrix([
        [5, -6],
        [8, 10]
    ]),

    'Ex 1b': sp.Matrix([
        [1 - x, -x],
        [x, 1 - x]
    ]),

    'Ex 2a': sp.Matrix([
        [2, 3, 4],
        [-2, -1, 1],
        [5, 3, 2]
    ]),

    'Ex 2b': sp.Matrix([
        [3, 15, 7],
        [0, -4, 0],
        [3, 2, 3]
    ]),
}

for x in dict:
    print(x, '\n', dict[x])
    determinant = sp.det(dict[x])
    try:
        determinant = sp.det(dict[x])
    except Exception:
        pass
    print(f'determinant = {determinant} \n')