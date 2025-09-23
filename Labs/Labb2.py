import matplotlib.pyplot as plt
import numpy as np

width = []
height = []
label = []

with open("Labs/datapoints.txt", "r") as file:
    next(file)
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            width.append(float(parts[0]))
            height.append(float(parts[1]))
            label.append(int(parts[2]))

data_points = np.array(list(zip(width, height)))
full_labels = np.array(label)

indices = np.arange(len(data_points))
np.random.shuffle(indices)
data_points = data_points[indices]
full_labels = full_labels[indices]

pichu_count = np.sum(full_labels == 0)
pikachu_count = np.sum(full_labels == 1)

if pichu_count >= 75 and pikachu_count >= 75:
    train_points = np.concatenate([data_points[full_labels == 0][:50], data_points[full_labels == 1][:50]])
    train_labels = np.concatenate([full_labels[full_labels == 0][:50], full_labels[full_labels == 1][:50]])
    test_points = np.concatenate([data_points[full_labels == 0][50:75], data_points[full_labels == 1][50:75]])
    test_labels = np.concatenate([full_labels[full_labels == 0][50:75], full_labels[full_labels == 1][50:75]])
else:
    train_points = data_points
    train_labels = full_labels
    test_points = np.array([])
    test_labels = np.array([])

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

predictions = [knn_classify(point, train_points, train_labels, k) for point in test_points]

if len(test_labels) > 0:
    TP = sum((p == 1 and a == 1) for p, a in zip(predictions, test_labels))
    TN = sum((p == 0 and a == 0) for p, a in zip(predictions, test_labels))

    accuracy = (TP + TN) / len(test_labels)

    print(f"TP = {TP}, TN = {TN}")
    print(f"Accuracy = {accuracy:.2f}")

testx = []
testy = []

with open("Labs/testpoints.txt", "r") as file:
    for line in file:
        if "(" in line:
            coords = line[line.find("(")+1 : line.find(")")].split(",")
            testx.append(float(coords[0]))
            testy.append(float(coords[1]))

test_points_cord = np.array(list(zip(testx, testy)))

predictions_external = [knn_classify(point, train_points, train_labels, k) for point in test_points_cord]
for (x_cord, y_cord), pred in zip(test_points_cord, predictions_external):
    print(f"Test point ({x_cord}, {y_cord}) identified as: {label_names[pred]}")

#print("Datapunkter", np.array(list(zip(width, height, label))))
print("Testpunkter:", list(zip(testx, testy)))

#Fixa h
plt.scatter([w for (w, h), l in zip(train_points, train_labels) if l == 0], [h for (w, h), l in zip(train_points, train_labels) if l == 0], color = "black", label = "Pichu", alpha = 0.5)
plt.scatter([w for (w, h), l in zip(train_points, train_labels) if l == 1], [h for (w, h), l in zip(train_points, train_labels) if l == 1], color = "yellow", label = "Pikachu", alpha = 0.5)

if len(test_points) > 0:
    for (x, y), pred, actual in zip(test_points, predictions, test_labels):
        if pred == actual:
            plt.scatter(x, y, color = "green", alpha = 0.5, marker = "x")
        else:
            plt.scatter(x, y, color = "red", alpha = 0.5, marker = "x")

plt.scatter(testx, testy, color = "orange", label = "Testpoints")

plt.title("Pichu vs Pikachu")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()

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
        predicted_label = knn_classify(user_point, train_points, train_labels, k)
        identification = label_names[predicted_label]

        print(f"Point ({width_input}, {height_input}) is identified as {identification}")

        plt.scatter(width_input, height_input, color = "blue", marker = "*", label = "User Input")
        plt.legend() 
        break

identify_user_input()
plt.show()