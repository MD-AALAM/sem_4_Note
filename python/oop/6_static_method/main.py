class Math:
    def __init__(self, num):
        self.num=num   
    
    def addtonum(self, n):
        self.num += n
    
    @staticmethod
    def add(a,b):
        return a + b

a= Math(10)
a.addtonum(5)
print(a.num)  # Output: 15
print(Math.add(3, 7))  # Output: 10 