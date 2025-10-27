def name_cleaner(name):
    return ' '.join(word.capitalize() for word in name.strip().split(","))

names = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "]
names_cleaned = [name_cleaner(name) for name in names]

for name in names_cleaned:
    print(name)