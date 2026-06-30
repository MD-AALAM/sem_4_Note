class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))   # calling original constructor


s1 = Student("Majid", 20)     # Normal constructor

s2 = Student.from_string("Ali-22")   # Alternative constructor

print(s2.name)   # Ali
print(s2.age)    # 22
