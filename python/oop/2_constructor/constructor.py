class person:
    def __init__(self, name, age):
        print("hey iam a person")
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = person("Alice", 30)
p1.info()

p2 = person("Bob", 25)
p2.info()

