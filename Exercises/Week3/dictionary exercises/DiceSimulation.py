import random as rnd

n = 1000000
counts = {i: 0 for i in range(1, 7)}

for _ in range(n):
    roll = rnd.randint(1, 6)
    counts[roll] += 1

for face in range(1, 7):
    print(f"{face}: {counts[face]}")