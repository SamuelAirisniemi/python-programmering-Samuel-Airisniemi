import numpy as np #impor till import

def distance(x,y): #Saknade ":"
    return np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2) #reuen till return och fixade formulan

print(f"The distance between (0.5, 0.5) and origin is around {distance([0.5, 0.5], [0, 0]):.3f}") #La till origin och avrundning