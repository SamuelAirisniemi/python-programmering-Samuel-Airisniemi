import matplotlib.pyplot as plt

path = "Labs/Labb3/unlabelled_data (1).csv"

x, y = [], []

with open(path, "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2:
            x_val, y_val = map(float, parts)
            x.append(x_val)
            y.append(y_val)

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Labb3")
plt.grid()
plt.show()