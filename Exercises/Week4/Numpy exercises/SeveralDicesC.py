import numpy as np

dice = np.arange(1, 7)

sum_matrix = dice[:, None] + dice[None, :]

sums = sum_matrix.flatten()

unique_sums, counts = np.unique(sums, return_counts=True)

frequencies = counts / counts.sum()

print("Unique values:")
print(unique_sums)
print("Counts:")
print(counts)
print("Frequencies:")
print(frequencies)
print("Check sum:")
print(frequencies.sum())