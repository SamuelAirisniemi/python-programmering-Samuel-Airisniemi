import random

print("Välkommen till multiplikationsspelet!")
print("Välj svårighetsgrad:")
print("1. Lätt (1-5)")
print("2. Medel (1-10)")
print("3. Svår (1-20)")

val = input("Ange 1, 2 eller 3: ")

if val == "1":
    min, max = 1, 5
elif val == "2":
    min, max = 1, 10
elif val == "3":
    min, max = 1, 20
else:
    print("Ogiltigt val, standard är Medel (1-10).")
    min, max = 1, 10

while True:

    x = random.randint(min, max)
    y = random.randint(min, max)

    guess = int(input(f"Vad är {x} multiplicerat med {y}? "))

    while guess != x * y:
        guess = int(input("Fel! Försök igen"))
    print("Rätt svar")

    spela_igen = input("Vill du spela igen? (J/N): ")
    if spela_igen.upper() != 'J':
        print("Tack för att du spelade!")
        break
    


