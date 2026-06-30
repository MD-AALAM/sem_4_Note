# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class (inherits Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object of child class
d = Dog()

# Access parent class method
d.speak()

# Access child class method
d.bark()
