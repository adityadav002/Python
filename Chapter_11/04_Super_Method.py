class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) 
        self.student_id = student_id
        print(f"Person ID: {self.student_id}")

s = Student("Alice", "S101")
