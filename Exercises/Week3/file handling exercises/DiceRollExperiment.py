import random as rnd
path = "Exercises/file handling exercises/simulation.txt"
simulations = [10, 100, 1000, 10000, 100000]

with open(path, "w") as f:
    for n in simulations:
        rolls = [rnd.randint(1, 6) for _ in range(n)]

        frequencies = {i: rolls.count(i) for i in range(1, 7)}

        f.write(f"Number of rolls: {n}\n")

        names = {
            1: "Ones",
            2: "Twos",
            3: "Threes",
            4: "Fours",
            5: "Fives",
            6: "Sixes"
        }

        for face in range(1, 7):
            freq = frequencies[face]
            prob = freq / n
            f.write(f"{names[face]}: {freq}, probability: {prob:.1f}\n")

        f.write("\n")