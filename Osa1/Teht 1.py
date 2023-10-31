import numpy as np

print('#1.a')
rad = 2.493
print(round(np.rad2deg(rad), 1))

print('\n#1.b')
rad = 0.911
print(round(np.rad2deg(rad), 1))

print('\n#2.a')
deg = 137.7
print(round(np.deg2rad(deg), 1))

print('\n#2.b')
deg = 62.3
print(round(np.deg2rad(deg), 1))


print(f'''
#3
+------+------+
| ast  | rad  |
+------+------+''')

deg = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]

for x in deg:
    rad = round(np.deg2rad(x), 2)
    if x < 100:
        print(f'| {x}   | {rad} |')
    if x >= 100:
        print(f'| {x}  | {rad} |')
    print('+------+------+')
