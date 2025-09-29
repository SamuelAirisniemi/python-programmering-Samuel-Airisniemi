table = input("Which table are you interested in? ")
start = int(input("Specify start of table: "))
end = int(input("Specify end of table: "))

print(f"Your {table + 'th'} multiplication table from {start} to {end}: ")

for i in range(start, end + 1):
    product = int(table) * i
    print(f"{product}", end=' ')