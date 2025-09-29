import matplotlib.pyplot as plt

def read_percentage_file(path):
    labels, values = [], []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                label, percent_str = parts
                value = float(percent_str.strip("%"))
                labels.append(label)
                values.append(value)
    return labels, values

labels1, values1 = read_percentage_file("Exercises/file handling exercises/NPvt19Ma2A.txt")
labels2, values2 = read_percentage_file("Exercises/file handling exercises/NPvt19Ma2C.txt")

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.pie(values1, labels=labels1)
ax1.set_title("NP Ma2A")

ax2.pie(values2, labels=labels2)
ax2.set_title("NP Ma2C")

plt.tight_layout()
plt.show()