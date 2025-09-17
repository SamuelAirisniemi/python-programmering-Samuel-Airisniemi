import random as rnd

dice_roll = [rnd.randint(1, 6) for i in range(100)]
antal_sexor = dice_roll.count(6)

print(f"Antalet sexor på hundra kast: {antal_sexor}")