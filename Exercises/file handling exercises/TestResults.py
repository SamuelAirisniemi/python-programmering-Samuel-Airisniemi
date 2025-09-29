path = "Exercises\file handling exercises\test_result.txt"

with open(path, "r") as f:
    text = f.read()

print(repr(text))