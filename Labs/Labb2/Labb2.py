import matplotlib.pyplot as plt
import numpy as np

#Läser in txt-fil och returnerar två arrayer med width, height och tillhärande label.
#Returnerar arrays
def load_data(filepath):
    widths, heights, labels = [], [], []
    with open(filepath, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                widths.append(float(parts[0]))
                heights.append(float(parts[1]))
                labels.append(int(parts[2]))
    return np.array(list(zip(widths, heights))), np.array(labels)

#Läser in testdata från en txt-fil med koordinater (x, y) och returnerar dem som float-värden.
#Returnerar arrays
def load_test(filepath):
    test_x, test_y = [], []
    with open(filepath, "r") as file:
        for line in file:
            if "(" in line:
                coordinates = line[line.find("(")+1 : line.find(")")].split(",")
                test_x.append(float(coordinates[0]))
                test_y.append(float(coordinates[1]))
    return np.array(list(zip(test_x, test_y)))

#Beräknar avståndet mellan en punkt och träningsdatan med knn genom de tio närmsta punkterna och ger labeln 0 eller 1.
def knn_classify(point, data_points, train_labels, k=10):
    distances = np.sqrt(((data_points - point)**2).sum(axis=1))
    nearest = distances.argsort()[:k]
    nearest_labels = train_labels[nearest]
    return 0 if np.sum(nearest_labels == 0) > np.sum(nearest_labels == 1) else 1

#Tar emot användarens koordinat input och klassifierar den med knn. Även felhantering beroende på input.
def identify_user_input():
    while True:
        user_input = input("Enter the x and y point separated by a comma: ").strip()
        if not user_input:
            print("Input can't be empty. Please try again.")
            continue
        parts = user_input.split(",")
        if len(parts) != 2:
            print("Please enter two numbers separated by a comma.")
            continue
        try:
            x, y = float(parts[0]), float(parts[1])
        except ValueError:
            print("Invalid input: please enter numeric values only.")
            continue
        if x < 0 or y < 0:
            print("Your input can not be negative. Please enter two positive numbers.")
            continue

        user_point = np.array([x, y])
        predicted_label = knn_classify(user_point, train_points, train_labels, k)
        print(f"Point ({x}, {y}) is identified as {label_names[predicted_label]}")
        return x, y

#Blandar datapunkter och skriver ut dom i omordnad ordning.
data_points, full_labels = load_data("Labs/datapoints.txt")

index = np.arange(len(data_points))
np.random.shuffle(index)
data_points = data_points[index]
full_labels = full_labels[index]

print("Datapunkter:", data_points)

#Använder 50 punkter för träning och 25 punkter för test från varje klass. 
#Definierar etikett-namn för klassificering.
if np.sum(full_labels == 0) >= 75 and np.sum(full_labels == 1) >= 75:
    train_points = np.concatenate([data_points[full_labels == 0][:50], data_points[full_labels == 1][:50]])
    train_labels = np.concatenate([full_labels[full_labels == 0][:50], full_labels[full_labels == 1][:50]])
    test_points = np.concatenate([data_points[full_labels == 0][50:75], data_points[full_labels == 1][50:75]])
    test_labels = np.concatenate([full_labels[full_labels == 0][50:75], full_labels[full_labels == 1][50:75]])
else:
    train_points, train_labels = data_points, full_labels
    test_points, test_labels = np.array([]), np.array([])

label_names = {0: "Pichu", 1: "Pikachu"}

#Beräkna accuracy med knn genom att summera True Positive och True Negatives och dela de med totalen.
k = 10

predictions = [knn_classify(p, train_points, train_labels, k) for p in test_points]

if len(test_labels) > 0:
    TP = sum((p == 1 and a == 1) for p, a in zip(predictions, test_labels))
    TN = sum((p == 0 and a == 0) for p, a in zip(predictions, test_labels))
    accuracy = (TP + TN) / len(test_labels)
    print(f"TP = {TP}, TN = {TN}")
    print(f"Accuracy = {accuracy:.2f}")

external_test_points = load_test("Labs/testpoints.txt")
external_predictions = [knn_classify(p, train_points, train_labels, k) for p in external_test_points]

for (x, y), pred in zip(external_test_points, external_predictions):
    print(f"Sample with (widht, height): ({x}, {y}) identified as {label_names[pred]}")

print("Testpunkter:", [f"({x:.1f}, {y:.1f})" for x, y in external_test_points])

#Extraherer x och y kordinater från träningspunkterna och skapar masker för att skilja på Pichu och Pikachu.
train_x, train_y = train_points[:, 0], train_points[:, 1]
mask_pichu = (train_labels == 0)
mask_pikachu = (train_labels == 1)

user_x, user_y = identify_user_input()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(train_x[mask_pichu], train_y[mask_pichu], color = "black", label = "Pichu", alpha = 0.5)
ax1.scatter(train_x[mask_pikachu], train_y[mask_pikachu], color = "yellow", label = "Pikachu", alpha = 0.5)

#Jämför varje förutsägelse med labeln och samlar korrekta och felaktiga punkter. 
#Markerar dem med grönt kryss om korrekt eller rött kryss om felaktigt.
if len(test_points) > 0:
    correct_points = []
    incorrect_points = []
    for (x, y), pred, actual in zip(test_points, predictions, test_labels):
        if pred == actual:
            correct_points.append((x, y))
        else:
            incorrect_points.append((x, y))

    if correct_points:
        correct_x, correct_y = zip(*correct_points)
        ax1.scatter(correct_x, correct_y, color = "green", marker = "x", label = "Correct")

    if incorrect_points:
        incorrect_x, incorrect_y = zip(*incorrect_points)
        ax1.scatter(incorrect_x, incorrect_y, color = "red", marker = "x", label = "Incorrect")

ax1.scatter(external_test_points[:, 0], external_test_points[:, 1], color = "orange", label = "Testpoints")
ax1.scatter(user_x, user_y, color = "blue", marker = "*", label = "User Input")

ax1.set_title("Pichu vs Pikachu")
ax1.set_xlabel("Width (cm)")
ax1.set_ylabel("Height (cm)")
ax1.legend()
ax1.grid()

#Utför 10 experiment för att mäta knn-modellens träffsäkerhet. 
#Varje gång blandas data, delar upp dom i träning/test och klassificerar dem.
#Beräknar accuracy som sparas i en lista.
accuracies = []
for i in range(10):
    index = np.arange(len(data_points))
    np.random.shuffle(index)
    shuffled_points = data_points[index]
    shuffled_labels = full_labels[index]

    train = np.concatenate([shuffled_points[shuffled_labels == 0][:50], shuffled_points[shuffled_labels == 1][:50]])
    loop_train_labels = np.concatenate([shuffled_labels[shuffled_labels == 0][:50], shuffled_labels[shuffled_labels == 1][:50]])
    test = np.concatenate([shuffled_points[shuffled_labels == 0][50:75], shuffled_points[shuffled_labels == 1][50:75]])
    loop_test_label = np.concatenate([shuffled_labels[shuffled_labels == 0][50:75], shuffled_labels[shuffled_labels == 1][50:75]])

    preds = [knn_classify(p, train, loop_train_labels, k) for p in test]
    TP = sum((p == 1 and a == 1) for p, a in zip(preds, loop_test_label))
    TN = sum((p == 0 and a == 0) for p, a in zip(preds, loop_test_label))
    acc = (TP + TN) / len(loop_test_label)
    accuracies.append(acc)

ax2.plot(range(1, 11), accuracies, marker = "o", color = "purple")
ax2.set_title("Accuracy for 10 tests")
ax2.set_xlabel("Tests")
ax2.set_ylabel("Accuracy")
ax2.grid()

print(f"Medium accuracy for 10 tests: {np.mean(accuracies):.2f}")

plt.tight_layout()
plt.show()