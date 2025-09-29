import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)

f = lambda x: x**2 - 3
g = lambda x: 4*x - 7

y_f = f(x)
y_g = g(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_f, color = "blue")
plt.plot(x, y_g, color = "orange")

plt.title("The function f(x) = x**2 - 3 and g(x) = 4x - 7")
plt.xlabel("x")
plt.ylabel("y")
plt.show()