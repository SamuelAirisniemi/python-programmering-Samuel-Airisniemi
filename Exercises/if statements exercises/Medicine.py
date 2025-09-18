age = int(input("Ange din ålder: "))
weight = int(input("Ange din vikt i kg: "))

if 3 <= age <= 7 and  15 <= weight <= 25:
    print("Du ska ta 1/2 tablett.")
elif age > 7 and weight < 26:
        print("Du ska ta 1/2 tablett.")
elif 7 <= age <= 12 and 25 < weight <= 40:
    print("Du ska ta 1/2-1 tablett.")
elif age <= 12 and weight > 40:
        print("Du ska ta 1-2 tabletter.")
elif age > 12 and weight > 40:
    print("Du ska ta 1-2 tabletter.")