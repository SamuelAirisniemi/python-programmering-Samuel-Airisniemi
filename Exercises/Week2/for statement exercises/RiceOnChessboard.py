import math

n = 0
riskorn = 1

for i in range(64):
    n += riskorn
    riskorn *= 2

print(f"{n}: Number of grains")