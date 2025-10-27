alphabet_lower = "abcdefghijklmnopqrstuvwxyzåäö"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

word = input("Skriv ett ord: ")
encrypted = ""

for char in word:
    if char in alphabet_lower:
        encrypted += alphabet_lower[(alphabet_lower.index(char) + 1) % len(alphabet_lower)] #Ändra till "-" för uppgift B
    elif char in alphabet_upper:
        encrypted += alphabet_upper[(alphabet_upper.index(char) + 1) % len(alphabet_upper)] #Samma här
    else:
        encrypted += char

print("Krypterat ord:", encrypted)