def is_fourdigit(number):
    abs_number = abs(number)            #Gör negativa tal positiva
    return 1000 <= abs_number <= 9999   #Kollar om de är fyrsiffriga

# test program
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")