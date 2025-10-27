import numpy as np

dice = np.arange(1, 7)
sum_matrix = dice[:, None] + dice[None, :]

print(sum_matrix)