class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Majid", 20)

print(s1.__dict__)
