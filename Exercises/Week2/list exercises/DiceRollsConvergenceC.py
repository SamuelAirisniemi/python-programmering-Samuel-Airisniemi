import random as rnd
import matplotlib.pyplot as plt

kast_lista = [10, 100, 1000, 10000, 100000, 1000000]
antal_sexor = []
sannorlikhet = []

for kast in kast_lista:
    rullningar = [rnd.randint(1, 6) for i in range(kast)]
    sexor = rullningar.count(6)
    antal_sexor.append(sexor)
    sannorlikhet.append(sexor / kast)

print("Antal kast:", kast_lista)
print("Antal sexor:", antal_sexor)
print("Sannolikhet för sexa:", sannorlikhet)

plt.plot(sannorlikhet, '-*')
plt.title("Probability of six for different number of rolls")
plt.xticks([0,1,2,3,4,5], antal_sexor)
plt.xlabel("Number of dice rolls")
plt.ylabel("Probability")
plt.show()