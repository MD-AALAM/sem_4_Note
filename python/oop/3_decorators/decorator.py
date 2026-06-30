# without an argument decorator
# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello World!")

# ->dono same baat
# hello()
# greet(hello)()


# with an argument decorator
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def add(x, y):
    print(f"The sum is: {x + y}")

# same baat
add(5,7)
# greet(add)(5,7)
