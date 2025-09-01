class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square: {self.n * self.n}")

    def cube(self):
        print(f"Cube: {self.n * self.n * self.n}")

    def squroot(self):
        print(f"Cube: {self.n**1/2}")
        
num = int(input("Enter a number: "))

result = Calculator(num)
result.cube()
result.square()
result.squroot()