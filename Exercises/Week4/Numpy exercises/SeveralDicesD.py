import numpy as np
import matplotlib.pyplot as plt

dice = np.arange(1, 7)

sum_matrix = dice[:, None] + dice[None, :]

sums = sum_matrix.flatten()

unique_sums, counts = np.unique(sums, return_counts=True)

frequencies = counts / counts.sum()

plt.figure(figsize=(8, 5))
plt.bar(unique_sums, frequencies, color = "blue")
plt.title("Two dices probability distributions")
plt.show()