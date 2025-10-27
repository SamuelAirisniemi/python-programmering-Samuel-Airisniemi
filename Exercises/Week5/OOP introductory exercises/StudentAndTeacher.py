class Person():
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self.email = email

    def say_hello(self):
        return (f"Hi, my name is {self.name}, I am  {self.age} years old, my email is {self.email}.")
    
class Student(Person):
    def study(self):
        return ("Study...study...study...more study.")
    
    def say_hello(self):
        return (f"Yo, i'm a student, my name is {self.name}, I am  {self.age} years old, my email is {self.email}.")

class Teacher(Person):
    def teach(self):
        return ("Teach...teach...teach...more teaching.")
    

teacher = Teacher("Pernilla", 32, "pernilla@gmail.com") 
student = Student("Karl", 25, "karl@gmail.com")

print(teacher.teach())
print(teacher.say_hello())
print(student.study())
print(student.say_hello())