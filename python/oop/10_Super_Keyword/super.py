class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()   # calling parent method
        print("This is Child class")

c1 = Child()
c1.show()
