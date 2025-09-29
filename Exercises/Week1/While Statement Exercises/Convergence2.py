n = 20
i = 0
sum_b = 0

while i < n:
    sum_b += ((-1) ** i) / (2 * i + 1)
    i += 1
print(sum_b)