import numpy as np
import matplotlib.pyplot as plt

sample_sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
means = []

for n in sample_sizes:
    rolls = np.random.randint(1, 7, size = n)
    means.append(rolls.mean())

plt.plot(sample_sizes, means, marker = "o", label = "Simulated mean")
plt.axhline(3.5, color="red", linestyle="--")
plt.xscale("log")
plt.xlabel("Number of rolls")
plt.ylabel("Sample mean")
plt.title("Mean of six-sided die")
plt.show()