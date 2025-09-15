import random as rnd

random_number = rnd.randint(1000, 9999)

for guess in range(1, 11):
    number = int(input("Gissa ett fyrsiffrigt nummer: "))
    if number < random_number:
        print("Din gissning var för låg. Gissa igen.")
    elif number > random_number:
        print("Din gissning var för hög. Gissa igen.")
    else:
        print(f"Grattis! Du gissade rätt nummer {random_number} på {guess} försök.")
        break
else:
    print(f"Du lyckades inte gissa rätt nummer. Det rätta numret var {random_number}.")