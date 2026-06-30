class Details:
    name="majid"
    age=20
    def desc(self):
        print(f"my Name is: {self.name} and my Age is : {self.age} years old")

# for user 1
a=Details()
a.desc()
# for user 2
b=Details()
b.name="ali"
b.age=22
b.desc()