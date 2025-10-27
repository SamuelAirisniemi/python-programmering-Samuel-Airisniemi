pokedex = {}
path = "Exercises\Week3\dictionary exercises\pokemon_list.txt"
with open(path, encoding="utf-8") as file:
    for line in file:
        part = line.strip().split(maxsplit=2)
        if len(part) == 3:
            index = part[0]
            namn = part[1]
            type = part[2]
            pokedex[namn] = f"{type}, {index}"

print(pokedex["Charizard"])
print(pokedex["Pikachu"])