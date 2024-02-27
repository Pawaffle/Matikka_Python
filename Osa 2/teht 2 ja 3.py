import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

X = np.linspace(-np.pi * 3, np.pi * 3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
fig = plt.figure(figsize=[4.8 * 3, 6.4 * 3])
xticks_values = np.arange(-3 * np.pi, 3 * np.pi + 1e-9, np.pi / 2)
xticks_labels = (r'$-3\pi$', r'$-5\pi/2$', r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$',
                 r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$',
                 r'$5\pi/2$', r'$3\pi$')

plt.plot(X,C)
plt.plot(X,S)
plt.xticks(xticks_values,xticks_labels)
plt.show()