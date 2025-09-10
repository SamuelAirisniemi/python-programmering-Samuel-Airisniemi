#import random
#random_number = random.randint(1, 100)

#guess = int(input("Gissa ett nummer mellan 1 och 100: "))

#while guess != random_number:
#    if guess < random_number:
#        print("För lågt! Försök igen.")
#    else:
#        print("För högt! Försök igen.")
#    guess = int(input("Gissa igen: "))

#print("Grattis! Du gissade rätt nummer.")

import random
random_number = random.randint(1, 100)

low = 1
high = 100
guess = (low + high) // 2

while guess != random_number:
    print(f"Jag gissar: {guess}")
    if guess < random_number:
        print("För lågt! Jag gissar högre.")
        low = guess + 1
    else:
        print("För högt! Jag gissar lägre.")
        high = guess - 1
    guess = (low + high) // 2

print(f"Jag gissade rätt nummer: {guess}")


#import random
#random_number = random.randint(1, 100)

#low = 1
#high = 100
#attempts = 0

#while low <= high:
    # Gissa både mitten och ett steg till (för att halvera antalet försök)
#    guess1 = (low + high) // 2
#    guess2 = guess1 + 1 if guess1 < high else guess1
#    attempts += 1

#    print(f"Jag gissar: {guess1}")
#    if guess1 == random_number:
#        print(f"Jag gissade rätt nummer: {guess1} på {attempts} försök!")
#        break
#    elif guess1 < random_number:
#        low = guess1 + 1
#    else:
#        high = guess1 - 1

    # Endast gissa guess2 om det är inom intervallet och guess1 inte var rätt
#    if low <= high and guess2 != guess1:
#        print(f"Jag gissar: {guess2}")
#        attempts += 1
#        if guess2 == random_number:
#            print(f"Jag gissade rätt nummer: {guess2} på {attempts} försök!")
#            break
#        elif guess2 < random_number:
#            low = guess2 + 1
#        else:
#            high = guess2