class Person():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not (isinstance(value, (int, float))):
            raise TypeError("Age must be an int or float.")
        if value < 0 or value > 125:
            raise ValueError("Age must be between 0 and 125.")
        self._age = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not (isinstance(value, str) and "@" in value and "." in value):
            raise TypeError(f"{value} is not a valid email, format should be xxx@yyy.zzz")
        self._email = value

    def __repr__(self):
        return (f"Person({self.name}, {self.age}, {self.email})")
    
    def say_hello(self):
        return (f"Hi, my name is {self.name}, I am  {self.age} years old, my email is {self.email}.")


p = Person("Pernilla", 32, "pernilla@gmail.com")
print(p)

try:
    p = Person("Pernilla", 32, "pernillagmail.com")
except TypeError as ex:
    print(ex)
except NameError as ex:
    print(ex)