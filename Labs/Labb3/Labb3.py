import matplotlib.pyplot as plt
import numpy as np

def point_position(x_point, y_point, k, m):
    y_line = k * x_point + m
    if y_point > y_line:
        vertical_position = "Above"
    elif y_point > y_line:
        vertical_position = "Below"
    else:
        vertical_position = "On"
    
    if k != 0:
        x_line = (y_point - m) / k
        if x_point > x_line:
            horizontal_position = "Right of"
        elif x_point < x_line:
            horizontal_position = "Left of"
        else:
            horizontal_position = "On"
    else:
        horizontal_position = "On"
    return (f"The point ({x_point}, {y_point}) is {vertical_position} and {horizontal_position} the line")

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

plt.plot(x_line, y_line, label = (f"y = {k}x + {m}"), color = "blue")
plt.scatter(x, y, label = "Data points", color = "Orange")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Labb3")
plt.grid()
plt.legend()
plt.show()

for x_point, y_point in zip(x, y):
    print(point_position(x_point, y_point, k, m))