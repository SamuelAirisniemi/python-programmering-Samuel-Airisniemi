import random as rnd

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