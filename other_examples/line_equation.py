# y = w*x + b
# w = weight [How steep the line is]
# b = bias

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-10, 10, 100)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# w = weight [ How steep the line is]
for weight, bias, color in [[2, 1, '-r'], [5, 1, '-.g'], [10, 1, ':b'], [15, 1, '--m']]:
    plt.plot(x, weight * x + bias, color, label=f'y={weight}x+{bias}')
plt.legend(loc='upper left')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-10, 10, 100)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# b = bias [ Shifting the line up and down]
for weight, bias, color in [[1, 1, '-r'], [1, 5, '-.g'], [1, 10, ':b'], [1, 15, '--m']]:
    plt.plot(x, weight * x + bias, color, label=f'y={weight}x+{bias}')
plt.legend(loc='upper left')
plt.show()
