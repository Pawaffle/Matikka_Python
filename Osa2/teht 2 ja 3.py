import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

X = np.linspace(-np.pi * 3, np.pi * 3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
fig = plt.figure(figsize=[4.8 * 3, 6.4 * 3])
x_ticks = [-3 np.pi, -2pi, -pi, 0, pi, 2pi, 3pi]

plt.plot(X,C)
plt.plot(X,S)

plt.show()