import matplotlib.pyplot as plt
import numpy as np

path = "Labs/Labb3/unlabelled_data (1).csv"

x, y = [], []

with open(path, "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2:
            x_val, y_val = map(float, parts)
            x.append(x_val)
            y.append(y_val)

k = -2
m = 0

x_line = np.linspace(min(x), max(x))
y_line = k * x_line + m

plt.plot(x_line, y_line)
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Labb3")
plt.grid()
plt.show()