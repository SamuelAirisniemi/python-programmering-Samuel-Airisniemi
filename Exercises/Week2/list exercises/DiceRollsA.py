import random as rnd

dice_roll = [rnd.randint(1, 6) for i in range(10)]

dice_roll.sort()

print(f"Ascending order: {dice_roll}")