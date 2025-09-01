class Employee:   # base class or parent class
    compnay = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name}, and the salary is {self.salary}")

class Programmer(Employee):   # derived class or child class
    company = "Infotech"
    def showLang(self):
        print(f"The name is {self.name}, and he is good with {self.language} language")

a = Employee
b = Programmer

print(a.compnay, b.company)