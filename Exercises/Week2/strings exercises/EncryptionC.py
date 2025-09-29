alphabet_lower = "abcdefghijklmnopqrstuvwxyzåäö"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

choice = input("Do you want to encrypt or decrypt? 1 or 2: ")
word = input("Enter a word: ")
result = ""

for char in word:
    if char in alphabet_lower:
        index = alphabet_lower.index(char)
        if choice == "1":
            result += alphabet_lower[(index + 1) % len(alphabet_lower)]
        else:
            result += alphabet_lower[(index - 1) % len(alphabet_lower)]
    elif char in alphabet_upper:
        index = alphabet_upper.index(char)
        if choice == "1":
            result += alphabet_upper[(index + 1) % len(alphabet_upper)]
        else:
            result += alphabet_upper[(index - 1) % len(alphabet_upper)]
    else:
        result += char

print("Result:", result)