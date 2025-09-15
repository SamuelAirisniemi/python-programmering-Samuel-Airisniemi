n = int(input("Enter a number for n!: "))
sum = 1

for i in range(1, n + 1):
    sum *= i

print(f"{n}! = {sum}")