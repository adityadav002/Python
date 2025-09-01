class Employee:
    language = 'Python'  # class attribute
    salary = 4000000

details = Employee()
details.name = "Aditya" # instance attributes , more preference than class attribute
details.language = "React"
print(details.name, details.language, details.salary)
