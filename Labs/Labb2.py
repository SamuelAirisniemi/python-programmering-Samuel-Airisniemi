import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

widht = []
height = []
label = []
testx = []
testy = []

with open("Labs/datapoints.txt", "r") as file:
    next(file)
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            widht.append(float(parts[0]))
            height.append(float(parts[1]))
            label.append(int(parts[2]))

with open("Labs/testpoints.txt", "r") as file:
    for line in file:
        if "(" in line:
            coords = line[line.find("(")+1 : line.find(")")].split(",")
            testx.append(float(coords[0]))
            testy.append(float(coords[1]))

data_points = np.array(list(zip(widht, height)))
train_labels = np.array(label)
test_points = np.array(list(zip(testx, testy)))
label_names = {0: "Pichu", 1: "Pikachu"}

k = 10
def knn_classify(point, data_points, train_labels, k = 10):
    distances = np.sqrt(((data_points - point)**2).sum(axis=1))
    nearest_neighbours = distances.argsort()[:k]
    nearest_labels = train_labels[nearest_neighbours]
    num_pichu = np.sum(nearest_labels == 0)
    num_pikachu = np.sum(nearest_labels == 1)

    if num_pichu > num_pikachu:
        return 0
    else:
        return 1

predictions = [knn_classify(point, data_points, train_labels, k) for point in test_points]

for (x_cord, y_cord), pred in zip(test_points, predictions):
    print(f"Test point ({x_cord}, {y_cord}) identified as: {label_names[pred]}")

print("Datapunkter", np.array(list(zip(widht, height, label))))
print("Testpunkter:", list(zip(testx, testy)))

def identify_user_input():
    while True:
        user_input = input("Enter the x and y point separated by a comma: ").strip()
        if not user_input:
            print("Input can't be empty. Please try again!")
            continue
        parts = user_input.split(",")
        if len(parts) != 2:
            print("Please enter two numbers separated by a comma.")
            continue

        try:
            width_input = float(parts[0].strip())
            height_input = float(parts[1].strip())
        except ValueError:
            print("Invalid input: please enter numeric values only.")
            continue
        if width_input < 0 or height_input < 0:
            print("Your input can not be negative. Please enter two positive numbers.")
            continue

        user_point = np.array([width_input, height_input])
        nearest_index = knn_classify(user_point, data_points, train_labels, k)
        identification = label_names[train_labels[nearest_index]]

        print(f"Point ({width_input}, {height_input}) is identified as {identification}")

        plt.scatter(width_input, height_input, color = "blue", marker = "*", label = "User Input")
        plt.legend() 
        break

plt.scatter([w for w, l in zip(widht, label) if l == 0], [h for h, l in zip(height, label) if l == 0], color = "black", label = "Pichu", alpha = 0.5)
plt.scatter([w for w, l in zip(widht, label) if l == 1], [h for h, l in zip(height, label) if l == 1], color = "yellow", label = "Pikachu", alpha = 0.5)
plt.scatter(testx, testy, color = "red", marker = "*", label = "Testpunkter")
plt.title("Pichu vs Pikachu")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
identify_user_input()
plt.show()