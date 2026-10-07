class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, {self.name}! I am {self.age} years old")

person1 = Person(name= "Alejna", age=14)
person2 = Person(name= "Yllka", age= 28)

person1.greet()
person2.greet()