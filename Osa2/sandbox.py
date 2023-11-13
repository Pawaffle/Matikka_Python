import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

fig, ax = plt.subplots(2,2)

x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]

ax[0, 1].plot(x, y, label='damn')
ax[0, 1].set_title('Font', fontsize=20)

ax[1, 0].plot(x, y, marker='*', alpha=0.5)

ax[0,1].legend(loc='best')

plt.show()