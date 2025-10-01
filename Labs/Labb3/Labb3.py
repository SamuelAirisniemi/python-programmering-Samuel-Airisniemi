import matplotlib.pyplot as plt
import numpy as np

def point_side(x_point, y_point, k, m):
    x1, y1 = 0, m
    x2, y2 = 1, k*1 + m

    cross = (x2 - x1) * (y_point - y1) - (y2 - y1) * (x_point - x1)

    if cross > 0:
        return 1
    else:
        return 0
    
unlabelled = "Labs/Labb3/unlabelled_data (1).csv"
labelled = "Labs/Labb3/labelled_data.csv"

x, y = [], []

with open(unlabelled, "r") as f_read:
    for line in f_read:
        parts = line.strip().split(",")
        if len(parts) == 2:
            x_val, y_val = map(float, parts)
            x.append(x_val)
            y.append(y_val)

k = -2
m = 0

with open(labelled, "w") as f_write:
    for x_point, y_point in zip(x, y):
        side = point_side(x_point, y_point, k, m)
        f_write.write(f"({x_point:.1f}, {y_point:.1f}), {side}\n")

x_line = np.linspace(min(x), max(x))
y_line = k * x_line + m

x_left = [xi for xi, yi in zip(x, y) if point_side(xi, yi, k, m) == 0]
y_left = [yi for xi, yi in zip(x, y) if point_side(xi, yi, k, m) == 0]
x_right = [xi for xi, yi in zip(x, y) if point_side(xi, yi, k, m) == 1]
y_right = [yi for xi, yi in zip(x, y) if point_side(xi, yi, k, m) == 1]

plt.figure(figsize=(8, 6))
plt.plot(x_line, y_line, label = (f"y = {k}x + {m}"), color = "blue")
plt.scatter(x_left, y_left, color = "red", label = "Vänster (0)")
plt.scatter(x_right, y_right, color = "green", label = "Höger (1)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Labb 3")
plt.grid()
plt.legend()
plt.show()