number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Talet är jämt")
else:
    print("Talet är ojämt")

if number % 5 == 0:
    print("Talet är delbart med 5")

if number % 5 == 0 and number % 2 != 0:
    print("Talet är delbart med 5 och är ojämt")