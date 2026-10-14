class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: woof")

class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: meow")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: chirp")

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

for animal in [dog, cat, bird]:
    animal.sound()