import numpy as np

n_rolls = 1000000
rolls = np.random.randint(1, 7, size = n_rolls)

simulated_mean = rolls.mean()

print(f"Simulated mean: {simulated_mean:.1f}")