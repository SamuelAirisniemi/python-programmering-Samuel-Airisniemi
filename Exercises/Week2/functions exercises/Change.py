def currency(amount):
    units = [
        (1000, "1000-lapp"),
        (500, "500-lapp"),
        (200, "200-lapp"),
        (100, "100-lapp"),
        (50, "50-lapp"),
        (20, "20-lapp"),
        (10, "10-krona"),
        (5, "5-krona"),
        (2, "2-krona"),
        (1, "1-krona")
    ]

    for value, label in units:
        count = amount // value
        if count:
            print(f"{count}st {label}")
        amount %= value

user_amount = int(input("Ange ett belopp i kronor: "))
currency(user_amount)