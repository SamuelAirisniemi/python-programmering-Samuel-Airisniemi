num = int(input("Skriv in ett nummer: "))

if num % 2 == 0 and num % 5 == 0:
    print(f"Numret {num} är jämnt och delbart med 5.")
elif num % 2 != 0 and num % 5 == 0:
    print(f"Numret {num} är udda och delbart med 5.")
elif num % 2 == 0:
    print(f"Numret {num} är jämnt men inte delbart med 5.")
else:
    print(f"Numret {num} är udda och inte delbart med 5.")