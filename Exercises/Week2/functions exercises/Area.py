def triangle(base, height):
    return (base * height)/2

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = triangle(base, height)
print(f"The area of the triangle is. {area}")