import numpy as np

dice = np.arange(1, 7)
sum_matrix = dice[:, None] + dice[None, :]
sums = sum_matrix.flatten()
unique_sums, counts = np.unique(sums, return_counts = True)

print("Unique Values:")
print(unique_sums)
print("Count:")
print(counts)