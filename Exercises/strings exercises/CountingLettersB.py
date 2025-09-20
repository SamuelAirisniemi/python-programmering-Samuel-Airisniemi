word = input("Enter a word: ")
print("Uppercase letters:", sum(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in word))
print("Lowercase letters:", sum(c in "abcdefghijklmnopqrstuvwxyz" for c in word))