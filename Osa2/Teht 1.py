from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr
import matplotlib as mpl

plt.style.use('dark_background')

fig = plt.figure() #figsize=[4.8 * 3, 6.4 * 3]
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)
ax.set_title('Matikan python tehtävä', color='orange', fontsize=15)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

pist_xy = np.array([np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi*2/3, np.pi*5/6, np.pi, np.pi*3/2])
name_xy = [r'$\pi/6$', r'$\pi/4$', r'$\pi/3$', r'$\pi/2$', r'$2\pi/3$', r'$5\pi/6$', r'$\pi$', r'$3\pi/2$']

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, color='orange', marker='o')

n = 0
h = 2
rl = 15

for i in pist_xy:
    plt.annotate(name_xy[n],
                 xy=(np.cos(i), np.sin(i)), xycoords='data',
                 xytext=(rl, h), textcoords='offset points',
                 fontsize=12, color='green')
    n += 1
    if n == 4: rl *= -2
    if n > 4: h -= 6


plt.show()