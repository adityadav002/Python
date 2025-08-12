class Animal:     # parent class.
    def __init__(self, name):
        self.name = name 

class Dog(Animal):   # child class 1.
    def speak(self):
        print(f"{self.name}, says woof woof!!!")
        print(f"{self.name}, eat bone")

class Cat(Animal):    # child class 2.
    def speak(self):
        print(f"{self.name}, says meow meow!!!")
        print(f"{self.name}, eat fish")

pet1 = Dog("Rocky")
pet2 = Cat("Rani")
pet1.speak()
print()
pet2.speak()