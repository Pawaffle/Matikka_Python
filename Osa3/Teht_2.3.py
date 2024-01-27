import numpy as np

# Sinulla on vektorit
# a) u = 2i + 3j, v =4i - 7j
# b) uu= i + j + k, vv 3i -3j + 2k.
# Määrittele nämä numpy taulukon avulla.

# Määritellään vektorit u ja v
u = np.array([2, 3])
v = np.array([4, -7])

# Määritellään vektorit uu ja vv
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

print('u: ', np.linalg.norm(u))
print('v: ', np.linalg.norm(v))
print('uu: ', np.linalg.norm(uu))
print('vv: ', np.linalg.norm(vv))