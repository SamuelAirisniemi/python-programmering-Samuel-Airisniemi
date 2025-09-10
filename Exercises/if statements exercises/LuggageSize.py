weight = int(input("Ange vikten på ditt bagage i kg: "))
lenght = int(input("Ange längden på ditt bagage i cm: "))
width = int(input("Ange bredden på ditt bagage i cm: "))
height = int(input("Ange höjden på ditt bagage i cm: "))

if weight > 8:
    print("Ditt bagage väger för mycket.")
if lenght > 55 or width > 40 or height > 23:
    print("Ditt bagage är för stort.")
else:
    print("Ditt bagage är godkänt.")