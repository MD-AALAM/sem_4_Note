#Exaple:1
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

d = Dog()
d.sound()

#Example:2
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        super().sound()   # parent method
        print("Dog barks")

d = Dog()
d.sound()
