import numpy as np
import matplotlib.pyplot as plt

width = []
height = []
labels = []

with open("Labs/datapoints.txt", "r") as file:
    next(file)  
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            width.append(float(parts[0]))
            height.append(float(parts[1]))
            labels.append(int(parts[2]))

data_points = np.array(list(zip(width, height)))
labels = np.array(labels)


indices = np.arange(len(data_points))
np.random.shuffle(indices)
data_points = data_points[indices]
labels = labels[indices]


train_points = np.concatenate([data_points[labels == 0][:50], data_points[labels == 1][:50]])
train_labels = np.concatenate([labels[labels == 0][:50], [labels == 1][:50]])

test_points = np.concatenate([data_points[labels == 0][50:75], data_points[labels == 1][50:75]])
test_labels = np.concatenate([labels[labels == 0][50:75], labels[labels == 1][50:75]])


def knn_classify(point, data_points, train_labels, k=10):
    distances = np.sqrt(((data_points - point)**2).sum(axis=1))
    nearest_neighbours = distances.argsort()[:k]
    nearest_labels = train_labels[nearest_neighbours]
    return 0 if np.sum(nearest_labels == 0) > np.sum(nearest_labels == 1) else 1

predictions = [knn_classify(p, train_points, train_labels, k=10) for p in test_points]

TP = sum((p == 1 and a == 1) for p, a in zip(predictions, test_labels))
TN = sum((p == 0 and a == 0) for p, a in zip(predictions, test_labels))

accuracy = (TP + TN) / len(test_labels)

print(f"TP = {TP}, TN = {TN}")
print(f"Accuracy = {accuracy:.2f}")

plt.scatter(
    [w for (w, h), l in zip(train_points, train_labels) if l == 0],
    [h for (w, h), l in zip(train_points, train_labels) if l == 0],
    color="black", label="Pichu (train)", alpha=0.5
)
plt.scatter(
    [w for (w, h), l in zip(train_points, train_labels) if l == 1],
    [h for (w, h), l in zip(train_points, train_labels) if l == 1],
    color="yellow", label="Pikachu (train)", alpha=0.5
)


for (x, y), pred, actual in zip(test_points, predictions, test_labels):
    if pred == actual:
        plt.scatter(x, y, color="green", marker="*", s=100)
    else:
        plt.scatter(x, y, color="red", marker="x", s=100)

plt.title("Pichu vs Pikachu (KNN)")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
plt.show()