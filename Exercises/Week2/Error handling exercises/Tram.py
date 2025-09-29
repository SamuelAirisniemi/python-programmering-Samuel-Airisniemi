def identify_user_input():
    while True:
        try:
            user_input = int(input("How many times do you take the tram in one month? "))
            if 0 <= user_input <= 100:
                return user_input
            else:
                print("Number of times must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

def ticket_cost():
    while True:
        try:
            cost_input = float(input("How much does one ticket cost? (kr) "))
            if 0 <= cost_input <= 100:
                return cost_input
            else:
                print("One ticket must cost between 0 and 100 kr.")
        except ValueError:
            print("Please enter a valid number.")

def month_cost():
    while True:
        try:
            monthly_price = float(input("How much does one month card cost? (kr) "))
            if 0 <= monthly_price <= 1000:
                return monthly_price
            else:
                print("One month card should cost between 0 and 1000 kr.")
        except ValueError:
            print("Please enter a valid number.")

rides = identify_user_input()
ticket_price = ticket_cost()
monthly_price = month_cost()

total_ticket_cost = rides * ticket_price

print(f"\nCost of one-time tickets: {total_ticket_cost:.1f} kr")
print(f"Cost with monthly card: {monthly_price:.1f} kr")

if monthly_price < total_ticket_cost:
    print("It's worth buying a monthly card.")
else:
    print("It's not worth buying a monthly card.")