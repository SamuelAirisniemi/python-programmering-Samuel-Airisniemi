import matplotlib.pyplot as plt
import numpy as np

x = np.array([-1, 1])
y = np.array([-1, 1])

d = ((x**2 + y**2))**0.5

plt.plot(x, y)
plt.show()