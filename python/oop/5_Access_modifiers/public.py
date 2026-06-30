class Student:
    def __init__(self, name):
        self.name = name   # public variable

    def show(self):        # public method
        print("Name:", self.name)

s = Student("Majid")
s.show()
print(s.name)
