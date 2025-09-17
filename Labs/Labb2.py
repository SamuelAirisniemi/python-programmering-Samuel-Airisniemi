import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

df = pd.read_csv("Labs/datapoints.txt")
df.columns = df.columns.str.strip()

x = df["(width (cm)"]
y = df["height (cm)"]
z = df["label (0-pichu"]

test_x = []
test_y = []

with open("Labs/testpoints.txt", "r") as f:
    for line in f:
        match = re.search(r"\(([\d\.]+),\s*([\d\.]+)\)", line)
        if match:
            test_x.append(float(match.group(1)))
            test_y.append(float(match.group(2)))

plt.scatter(x[z == 0], y[z == 0], color = "black", label = "Pichu", alpha = 0.5)
plt.scatter(x[z == 1], y[z == 1], color = "yellow", label = "Pikachu", alpha = 0.5)
plt.scatter(test_x, test_y, color = "red", label = "Testpunkter")

plt.title("Pichu vs Pikachu")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
plt.show()

print(df.head())
print("Testpunkter:", list(zip(test_x, test_y)))