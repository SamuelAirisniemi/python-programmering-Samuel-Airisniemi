path = "Exercises/file handling exercises/test_result.txt"

def grades(score):
    if score < 20:
        return "F"
    elif score < 30:
        return "E" 
    elif score < 40:
        return "D"
    elif score < 50:
        return "C"
    elif score < 60:
        return "B"
    else:
        return "A"

names = []

with open(path, "r", encoding="utf-8") as f_read:
    for line in f_read:
        parts = line.strip().split()
        if parts:
            name = " ".join(parts[:-1])
            score = int(parts[-1])
            names.append((name, score))

for name, score in names:
    print(f"{name} {score}")

sorted_names = sorted(names)

print("\nSorted alphabetically:")
for name, score in sorted_names:
    print(f"{name} {score}")

grade_groups = {"F": [], "E": [], "D": [], "C": [], "B": [], "A": []}

for name, score in names:
    grade = grades(score)
    grade_groups[grade].append((name, score))

print("\nSorted Results:")
for grade in ["F", "E", "D", "C", "B", "A"]:
    if grade_groups[grade]:
        print(f"Grade: {grade}")
        for name, score in grade_groups[grade]:
            print(f"{name} {score}")