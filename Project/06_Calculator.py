class Calculator:
    def __init__(self):
        print("Calculator is ready!")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

calc = Calculator()

while True:
    print("\nOptions: add, subtract, multiply, divide, exit")
    operation = input("Enter operation: ").lower()

    if operation == "exit":
        print("Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if operation == "add":
        print("Result:", calc.add(num1, num2))
    elif operation == "subtract":
        print("Result:", calc.subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", calc.multiply(num1, num2))
    elif operation == "divide":
        print("Result:", calc.divide(num1, num2))
    else:
        print("Unknown operation.")
