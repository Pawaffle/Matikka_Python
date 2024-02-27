import numpy as np

dict = {
    'A': np.array([
        [1, 2, 3],
        [1, 0, -2]
    ]),
    'B': np.array([
        [1],
        [4],
        [2]
    ]),
    'C': np.array([
        [1, 0, 2]
    ])
}

lst = ['A', 'B', 'C']

for x in lst:
    for y in lst:
        if x != y:
            try:
                ans = np.dot(dict[x], dict[y])
                print(f'{x}{y} \n {ans} \n')
            except:
                print(f'{x}{y} - not solvable \n')
