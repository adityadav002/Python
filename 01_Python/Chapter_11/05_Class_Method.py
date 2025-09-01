class Student:
    school_name = "Greenwood High"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    def show(self):
        print(f"Student: {self.name}, School: {Student.school_name}")

s1 = Student("Alice")

s1.show()  
s1.change_school("Sunrise Public School")
s1.show() 

