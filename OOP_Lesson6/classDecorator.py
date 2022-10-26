class Functor:
    def __call__(self, a, b):
        print(a * b)

f = Functor()
f(10, 20)

# Decorator example
class MyDecorator:
    def __init__(self, function):
        self.function = function
        
    def __call__(self):
        # before function call
        
        self.function()
        
        # after function call
        
@MyDecorator
def function():
    print("Function")
    
function()


# Decorator with args, kwargs
class MyDecorator:
    def __init__(self, function):
        self.function = function
        
    def __call__(self, *args, **kwargs):
        # before function call
        self.function(*args, **kwargs)
        # after function call
        

@MyDecorator
def func(name, message="Hello"):
    print(f"{message} {name}")
    
func("Alex", "hello")


# Decorator with return statement
class SquareDecorator:
    def __init__(self, function):
        self.function = function
        
    def __call__(self, *args, **kwargs):
        print("Before")
        result = self.function(*args, *kwargs)
        print("After")
        
        return result
    
@SquareDecorator
def square(n):
    print("Num is: ", n)
    return n * n
        
print(square(10))


# Timer decorator
from time import time
class Timer:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.func(*args, **kwargs)
        end_time = time()
        print(f"Execution took {end_time - start_time} seconds")
        
        return result
    
@Timer
def function(delay):
    from time import sleep
    sleep(delay)

function(3)