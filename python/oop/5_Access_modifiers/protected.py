class Person:
    def __init__(self):
        self._age = 20   # protected variable

class Employee(Person):
    def show_age(self):
        print("Age:", self._age)

e = Employee()
e.show_age()
print(e._age)   # possible but not recommended
