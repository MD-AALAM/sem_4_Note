# ->one common use of decorators is to add logging to a function
# -> for example, you could use a decorator to log the arguments and reurn value of a function each time

# Note->1.*args->->to accept any number of positional arguments
#      2.**kwargs->->to accept any number of keyword arguments
import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def Decorated(*args, **kwargs):
        logging.info(f"calling{func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return Decorated

@log_function_call
def my_function(x,y):
    return x + y

my_function(3,4)