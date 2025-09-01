class Father:    # parent class 1
    def skills(self):
        print("Father: Driving, Understanding")

class Mother:   # parent class 1
    def skills(self):
        print("Mother: Cooking, Behaving")

class Child(Father, Mother):    # child class
    def skills(self):
        print("Inherit skills from father and mother")
        Father.skills(self)
        Mother.skills(self)
        print("Child: Gaming, Coding")

a = Child()
a.skills()