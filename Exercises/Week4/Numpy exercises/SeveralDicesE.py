import numpy as np
import matplotlib.pyplot as plt

def dice_sum_distribution(n_dice):
    outcomes = np.arange(1, 7)
    sums = outcomes
    for _ in range(n_dice - 1):
        sums = sums[:, None] + outcomes
        sums = sums.flatten()
    unique, counts = np.unique(sums, return_counts=True)
    freqs = counts / counts.sum()
    return unique, freqs

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for idx, n_dice in enumerate([1, 2, 3, 4]):
    unique, freqs = dice_sum_distribution(n_dice)
    axes[idx].bar(unique, freqs, color = "blue")
    axes[idx].set_title(f"Probability distributions of sum of {n_dice} dice")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()