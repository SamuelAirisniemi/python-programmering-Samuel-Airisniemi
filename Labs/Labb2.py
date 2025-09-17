import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Labs/datapoints.txt")
test_df = pd.read_csv("Labs/testpoints.csv")
df.columns = df.columns.str.strip()

x = df["(width (cm)"]
y = df["height (cm)"]
z = df["label (0-pichu"]
test_x = ["widht"]
test_y = ["height"]


plt.scatter(x[z == 0], y[z == 0], color = "black", label = "Pichu", alpha = 0.5)
plt.scatter(x[z == 1], y[z == 1], color = "yellow", label = "Pikachu", alpha=0.5)
plt.scatter(test_x, test_y, color = "red", label = "Test Points")

plt.title("Pichu vs Pikachu")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
plt.show()

print(df.head())
print("Test points:", list(zip(test_x, test_y)))