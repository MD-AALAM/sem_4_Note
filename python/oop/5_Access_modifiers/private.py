class Bank:
    def __init__(self):
        self.__balance = 5000   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank()
b.show_balance()

# print(b.__balance)  # ❌ Error

print(b._Bank__balance)  # accessing private variable (not recommended)
