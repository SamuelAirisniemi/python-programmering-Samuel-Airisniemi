from math import gcd

class Frac:
    def __init__(self, nominator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator can not be zero.")
        self.nominator = nominator
        self.denominator = denominator
        self.simplify()
    
    def simplify(self, value = None):
        if value is not None:
            factor = value // gcd(self.nominator, self.denominator)
            self.nominator = self.nominator * (factor // self.denominator)
            self.denominator = value
        else:
            common = gcd(self.nominator, self.denominator)
            self.nominator //= common
            self.denominator //= common
            if self.denominator < 0:
                self.nominator *= -1
                self.denominator *= -1
        return self
    
    def __str__(self):
        return (f"{self.nominator}/{self.denominator}")
    
    def mixed(self):
        whole, remainder = divmod(abs(self.nominator), self.denominator)
        sign = "-" if self.nominator < 0 else ""
        if whole == 0:
            return (f"{sign}{remainder}/{self.denominator}")
        elif remainder == 0:
            return (f"{sign}{whole}")
        else:
            return (f"{sign}{whole} {remainder}/{self.denominator}")
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if not isinstance(other, Frac):
            return NotImplemented
        num = self.nominator * other.denominator + other.nominator * self.denominator
        den = self.denominator * other.denominator
        return Frac(num, den)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if not isinstance(other, Frac):
            return NotImplemented
        num = self.nominator * other.denominator - other.nominator * self.denominator
        den = self.denominator * other.denominator
        return Frac (num, den)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if not isinstance(other, Frac):
            return NotImplemented
        num = self.nominator * other.nominator
        den = self.denominator * other.denominator
        return Frac(num, den)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if not isinstance(other, Frac):
            return NotImplemented
        if other.nominator == 0:
            raise ZeroDivisionError("Division by zero fraction.")
        num = self.nominator * other.denominator
        den = self.denominator * other.nominator
        return Frac(num, den)
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Frac(other, 1)
        if not isinstance(other, Frac):
            return NotImplemented
        return (self.nominator * other.denominator ==
                other.nominator * self.denominator)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)
    
print(Frac(1,2) + Frac(1,3))
print(Frac(1,2) - Frac(1,3))
print(Frac(7,6).mixed())
print(Frac(3,1) * Frac(1,2))
print(Frac(1,2) * 3)
print(Frac(1,4) + 2)
print(Frac(1,4) / Frac(1,2))
print(Frac(2,4) == Frac(1,2))

f = Frac(3,4)
f += 2
print(f)    