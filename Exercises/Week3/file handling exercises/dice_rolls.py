import random as rnd

path = "Exercises/file handling exercises/dice_rolls.txt"
dice_roll = [rnd.randint(1, 6) for i in range(20)]
sorted_rolls = sorted(dice_roll)
fours = [i+1 for i, roll in enumerate(dice_roll) if roll == 4]

with open(path, "w") as file:
    file.write("Simulate 20 dice rolls:\n")
    file.write(f"{dice_roll}\n\n")
    file.write("Sorted dice rolls\n")
    file.write(f"{sorted_rolls}\n\n")
    file.write(f"Number of fours: {len(fours)}")