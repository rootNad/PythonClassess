# point = (2, 4)
# print(point) # (2, 4)
# pointComplex = 1 + 3j
# point = {"x": 1, "y": 3}

# # Access
# print(point[0])
# print(point[1])

# # Try to update
# point[0] = 3 # Error


# from collections import namedtuple

# Point = namedtuple("Point", "x y")
# issubclass(Point, tuple)

# point = Point(2, 4)
# print(point)

# print(point.x)
# print(point.y)

# print(point[0])
# print(point[1])

# point.x = 100 # Error

# # Person example
# Person = namedtuple("Person", "name surname")
# john = Person("John", "Doe")
# Person(name="John", surname="Doe")


from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
    
p1 = Point(1, 1)
print(p1)

# VS class
class PointClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# Dataclass automated add magic methods to out class
import inspect
from pprint import pprint
pprint(inspect.getmembers(Point, inspect.isfunction))
pprint(inspect.getmembers(PointClass, inspect.isfunction))

# In dataclass we can add default values
@dataclass
class Point:
    x: int
    y: int = 0
    
from dataclasses import astuple, asdict
print(astuple(p1))
print(asdict(p1))

# immutable types
@dataclass(frozen=True)
class PointImmutable:
    x: int = 10
    y: int = 100
    
    
from enum import Enum
class Product(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3
    
    
class MarketItem():
    def __init__(self, product_type, cost):
        self.product_type = product_type
        self.cost = cost
    
mi1 = MarketItem(Product.SHIRT, 100)