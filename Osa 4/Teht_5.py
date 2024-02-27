import numpy as np

dict = {
    'A': np.array([
        [1, 0.5],
        [2, 1]
    ]),
    'B': np.array([
        [-1, -2],
        [2, 4]
    ])
}

lst = ['A', 'B']

for x in lst:
    for y in lst:
        if x != y:
            try:
                ans = np.dot(dict[x], dict[y])
                print(f'{x}{y} \n {ans} \n')
            except:
                print(f'{x}{y} - not solvable \n')
