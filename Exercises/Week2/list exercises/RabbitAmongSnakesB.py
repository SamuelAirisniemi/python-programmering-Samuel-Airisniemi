import random
import matplotlib.pyplot as plt

def hall_game(trials, switch):
    wins = 0
    for i in range(trials):
        doors = ["snake", "snake", "rabbit"]
        random.shuffle(doors)

        player_choice = random.randint(0, 2)

        possible_doors = [i for i in range(3) if i != player_choice and doors[i] == "snake"]
        opened_door = random.choice(possible_doors)

        if switch:
            remaining_doors = [i for i in range(3) if i not in (player_choice, opened_door)]
            player_choice = remaining_doors[0]

        if doors[player_choice] == "rabbit":
            wins += 1

    return wins / trials

trial_counts = [10, 100, 1000, 10000, 100000, 1000000]
stay_results = []
switch_results = []

for t in trial_counts:
    stay_results.append(hall_game(t, switch=False))
    switch_results.append(hall_game(t, switch=True))

plt.plot(trial_counts, stay_results, marker='o', label="Stay")
plt.plot(trial_counts, switch_results, marker='o', label="Switch")
plt.xscale("log")
plt.xlabel("Number of Simulations")
plt.ylabel("Proportion of Wins")
plt.title("Proportion of wins are 2/3 compared to 1/3 when switching")
plt.legend()
plt.grid(True)
plt.show()