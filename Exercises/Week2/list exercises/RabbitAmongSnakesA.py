import random as rnd

def hall_game():
    doors = ["snake", "snake", "rabbit"]
    rnd.shuffle(doors)

    print("There are 3 doors: 0, 1, 2")
    player_choice = int(input("Pick a door (0, 1, or 2): "))

    possible_doors = [i for i in range(3) if i != player_choice and doors[i] == "snake"]
    opened_door = rnd.choice(possible_doors)
    print(f"Door {opened_door} opens and you find a snake inside.")

    remaining_doors = [i for i in range(3) if i not in (player_choice, opened_door)]
    switch_choice = input(f"Do you want to switch to door {remaining_doors[0]}? (y/n): ").lower()

    if switch_choice == "y":
        player_choice = remaining_doors[0]

    print(f"You chose door {player_choice}. Behind it is a {doors[player_choice]}!")
    if doors[player_choice] == "rabbit":
        print("Congratulations! You found the rabbit!")
    else:
        print("Sorry, you got a snake.")

hall_game()