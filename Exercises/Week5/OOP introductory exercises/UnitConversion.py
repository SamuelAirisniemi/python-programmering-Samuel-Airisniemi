class US2Metric:
    def __init__(self, value):
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if not isinstance(v, (int, float)):
            raise TypeError("Value must be an int or float.")
        if v < 0:
            raise ValueError("Value must be non-negative.")
        self._value = float(v)

    def inch_to_cm(self):
        return self.value * 2.54

    def foot_to_meters(self):
        return self.value * 0.3048

    def pound_to_kg(self):
        return self.value * 0.45359237

    def __repr__(self):
        return f"US2Metric(value={self.value})"


units = US2Metric(5)
print(units)
print("5 inches in cm:", units.inch_to_cm())
print("5 feet in meters:", units.foot_to_meters())
print("5 pounds in kg:", units.pound_to_kg())

try:
    units.value = "abc"
except Exception as e:
    print("\nError:", e)

try:
    bad_converter = US2Metric(-5)
except Exception as e:
    print("Error:", e)