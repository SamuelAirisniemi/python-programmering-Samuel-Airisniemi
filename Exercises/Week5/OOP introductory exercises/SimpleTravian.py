class ResourceField:
    def __init__(self, name, production_rate=4, capacity=800):
        self.name = name
        self.production_rate = production_rate
        self.capacity = capacity
        self.stock = 500

    def __add__(self, amount):
        if not isinstance(amount, (int, float)):
            return NotImplemented
        self.stock = min(self.capacity, self.stock + amount)
        return self

    def __sub__(self, amount):
        if not isinstance(amount, (int, float)):
            return NotImplemented
        self.stock = max(0, self.stock - amount)
        return self

    def __repr__(self):
        return f"{self.name}: {self.stock}/{self.capacity}"


class Village:
    def __init__(self):
        self.lumber_field = ResourceField("Lumber")
        self.clay_field = ResourceField("Clay")
        self.iron_field = ResourceField("Iron")
        self.wheat_field = ResourceField("Crop")

    def __repr__(self):
        stock_repr = (
            f"Stock: "
            f"Lumber:{self.lumber_field.stock}/{self.lumber_field.capacity}\t "
            f"Clay:{self.clay_field.stock}/{self.clay_field.capacity}\t "
            f"Iron:{self.iron_field.stock}/{self.iron_field.capacity}\t "
            f"Crop:{self.wheat_field.stock}/{self.wheat_field.capacity}"
        )

        prod_repr = (
            f"Production:\n"
            f"Lumber: {self.lumber_field.production_rate} per hour\n"
            f"Clay: {self.clay_field.production_rate} per hour\n"
            f"Iron: {self.iron_field.production_rate} per hour\n"
            f"Crop: {self.wheat_field.production_rate} per hour"
        )

        return stock_repr + "\n" + prod_repr

if __name__ == "__main__":
    vill = Village()
    vill.wheat_field += 500
    vill.clay_field -= 25
    vill.lumber_field += 200
    print(vill)