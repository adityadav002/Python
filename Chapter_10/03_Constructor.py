class Employee:
    language = 'not filled'  # class attribute
    salary = None

    def __init__(self, name, language, salary):   # dunder method, which is automatically called (Constructor)
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):   # methods
        print(f"The name is {self.name}. \nThe Language is {self.language}. \nThe salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Thank you for submitting your info...")

emp_name = input("Enter Your name: ")
emp_lang = input("Enter Your language: ")
emp_sal = input("Enter Your salary: ")
details = Employee(emp_name, emp_lang, emp_sal)
print()
details.getInfo()
details.greet()
