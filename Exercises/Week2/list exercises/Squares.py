import matplotlib.pyplot as plt

square = [x**2 for x in range (-10, 11)]
print(square)

plt.plot(square)
plt.title("The function x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()