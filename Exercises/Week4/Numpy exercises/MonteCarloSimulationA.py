import numpy as np
import matplotlib.pyplot as plt

points = 500000

x = np.random.uniform(-1, 1, points)
y = np.random.uniform(-1, 1, points)

d = np.sqrt(x**2 + y**2)

inside = d < 1
outside = d >= 1

plt.figure(figsize=(8, 8))
plt.scatter(x[inside], y[inside], color = "blue")
plt.scatter(x[outside], y[outside], color = "orange")
plt.title("Simulation of 500,000 Points")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()