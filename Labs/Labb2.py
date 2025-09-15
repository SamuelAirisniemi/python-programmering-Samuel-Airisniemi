import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Labs\datapoints.txt")

x = df["(width (cm)"]
y = df[" height (cm)"]
z = df[" label (0-pichu"]

plt.scatter(x[z == 0], y[z == 0], color='black', label='Pichu', alpha = 0.5)
plt.scatter(x[z == 1], y[z == 1], color='yellow', label='Pikachu', alpha = 0.5)

plt.title("Pichu vs Pikachu")
plt.xlabel("Widht (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
plt.show()

#print(df.head())