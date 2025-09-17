import matplotlib.pyplot as plt

x = []
y = []
z = []

with open("Labs/datapoints.txt", "r") as f:
    next(f)  # Hoppa över rubrikraden
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 3:
            x.append(float(parts[0]))
            y.append(float(parts[1]))
            z.append(int(parts[2]))

test_x = []
test_y = []

with open("Labs/testpoints.txt", "r") as f:
    for line in f:
        if "(" in line:
            coords = line[line.find("(")+1:line.find(")")].split(",")
            test_x.append(float(coords[0]))
            test_y.append(float(coords[1]))

plt.scatter([a for a, b in zip(x, z) if b == 0], [a for a, b in zip(y, z) if b == 0], color="black", label="Pichu", alpha=0.5)
plt.scatter([a for a, b in zip(x, z) if b == 1], [a for a, b in zip(y, z) if b == 1], color="yellow", label="Pikachu", alpha=0.5)
plt.scatter(test_x, test_y, color="red", label="Testpunkter")

plt.title("Pichu vs Pikachu")
plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid()
plt.show()

print("Datapunkter:", list(zip(x, y, z)))
print("Testpunkter:", list(zip(test_x, test_y)))