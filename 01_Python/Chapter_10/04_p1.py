class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def getInfo(self):
        print(f"Company : {self.company}, \nName : {self.name}, \nSalary : {self.salary}, \nPin : {self.pin}.")


Details = Programmer("Aditya", 1200000000, "452010")
Details.getInfo()

