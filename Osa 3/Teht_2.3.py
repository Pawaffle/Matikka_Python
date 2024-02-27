import numpy as np

# Laske kunkin vektorin normi

u = np.array([2, 3])
v = np.array([4, -7])
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

print('u: ', np.linalg.norm(u))
print('v: ', np.linalg.norm(v))
print('uu: ', np.linalg.norm(uu))
print('vv: ', np.linalg.norm(vv))