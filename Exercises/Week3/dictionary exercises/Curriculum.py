words = {
    "Introduktionskurs": 5,
    "Programmering med Python": 40,
    "Examensarbete": 15,
    "Djup maskininlärning": 40,
    "Data Engineering och agila metoder": 45,
    "Databaser": 25,
    "Maskininlärning": 45,
    "Statistiska metoder": 30,
    "Linjär algebra": 20,
    "Databehandling": 25,
    "LIA 1": 40,
    "LIA 2": 70
}

print(f"\n\nKurser:{'':<33} YH-poäng:")
for key, value in words.items():
    print(f"{key:<40} {value}")

total_points = sum(words.values())
print("\nTotal YH-poäng:", total_points)