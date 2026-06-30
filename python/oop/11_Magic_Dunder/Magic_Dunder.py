#Example:1
#1️⃣ __init__() → Constructor
#Purpose:
#Used to initialize object variables.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Majid")

#✔ Automatically called when object is created.


#Example:2
#2️⃣ __str__() → String Representation (User Friendly)
#Used when we print the object.
class Student:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Student name is {self.name}"

s1 = Student("Majid")
print(s1)

#Without __str__():
#output=<__main__.Student object at 0x000...>

#With __str__():
#output=Student name is Majid


#Example:3
#3️⃣ __repr__() → Developer Representation
#Used for debugging.
#If __str__() is not defined, Python uses __repr__().


#Example:4
#4️⃣ __len__() → Length Function
#Used when we call len().
class MyClass:
    def __len__(self):
        return 10

obj = MyClass()
print(len(obj))   # 10
