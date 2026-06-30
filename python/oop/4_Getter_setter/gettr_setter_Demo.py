# getter example
# class Myclass:
#     def __init__(self,value):
#         self._value = value
    
#     def show(self):
#         print(f"Value is: {self._value}")

#     @property
#     def value(self):
#         return self._value
    
# obj=Myclass(10)
# obj.value
# obj.show()
# obj.value=20  # This will raise an AttributeError since there is no setter defined for 'value'


# setter example
class Myclass:
    def __init__(self,value):
        self._value = value
    
    def show(self):
        print(f"Value is: {self._value}")

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

obj=Myclass(10)
obj.value=20  # This will work now since setter is defined for 'value'
print(obj.value)
obj.show()