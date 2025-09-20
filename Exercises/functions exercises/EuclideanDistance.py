import math
def euclidean(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

x1 = int(input("Enter the first x point: "))
y1 = int(input("Enter the first y point: "))
p = (x1, y1)
x2 = int(input("Enter the second x point: "))
y2 = int(input("Enter the second y point: "))
q = (x2, y2)

distance = euclidean(p, q)

print(f"The distance between these two point are: {distance:.1f}")