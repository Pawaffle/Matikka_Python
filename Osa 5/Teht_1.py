import numpy as np

dict = {
    'A': np.array([
            [4, 9, 0],
            [-3, 7, -11]]
    ),

    'B': np.array([
            [8, 9],
            [-3, 12],
            [0, -1],
            [7, 1]
    ])
}

for x in dict:
    print(f'''
{x} = \n {dict[x]} 

"{x}" after the transpose  \n {dict[x].transpose()}
    ''')