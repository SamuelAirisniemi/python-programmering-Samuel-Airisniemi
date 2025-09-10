age = int(input("Ange din ålder: "))
weight = int(input("Ange din vikt i kg: "))

if age >= 3 and age <= 7 and weight >= 15 and weight <= 25:
    print("Du ska ta 1/2 tablett.")
elif age > 7 and weight < 26:
        print("Du ska ta 1/2 tablett.")
elif age >= 7 and age <= 12 and weight > 25 and weight <= 40:
    print("Du ska ta 1/2-1 tablett.")
elif age <= 12 and weight > 40:
        print("Du ska ta 1-2 tabletter.")
elif age > 12 and weight > 40:
    print("Du ska ta 1-2 tabletter.")