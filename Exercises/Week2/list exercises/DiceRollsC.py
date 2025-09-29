import random as rnd

dice_roll = [rnd.randint(1, 6) for i in range(10)]

dice_roll.sort(reverse = True)

print(f"Maximum: {dice_roll[0]}")
print(f"Lowest: {dice_roll[-1]}")