from matplotlib import pyplot as plt

import numpy as np

fig, axes = plt.subplots(2,1)

# PI * 10, 너비에 500개 점 찍기 (0 ~ 31.4 사이에 500개의 점을 찍겠다.)
x = np.linspace(0, np.pi * 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)

axes[0].plot(x, y1)
axes[1].plot(x, y2)

plt.show()
