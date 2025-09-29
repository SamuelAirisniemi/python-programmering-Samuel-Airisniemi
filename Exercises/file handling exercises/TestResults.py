path = "Exercises/file handling exercises/test_result.txt"
persons, i = [], 1

with open(path, "r") as f:
    people = [line.strip() for line in f if line.strip()]
    #text = f.read()

print(people)