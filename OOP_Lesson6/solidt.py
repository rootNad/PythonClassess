# DESIGN PRINCIPLES

# Composition instead of inheritance
# Inheritance
class Parent:
    def m1(self):
        print("Parent class method called")
        
class Child(Parent):
    def __init__(self):
        print("Child Class object created")

    def m2(self):
        print("Child class Method called")
        
obj = Child()
obj.m1()
obj.m2()

# Composition
class Component():
    def __init__(self):
        print("Component class object created")
    
    def m1(self):
        print("Component class m1() method executed")
        
class Composite():
    def __init__(self):
        self.obj1 = Component()
        print("Composite class object created")
    
    def m2(self):
        print("Composite class m2() method executed")
        self.obj1.m1()
        
obj2 = Composite()
obj2.m2()    

# YAGNI
# You Aren't Gonna Need It

# DRY
# Don't Repeat Yourself

# KISS
# Keep It Simple, Stupid

# BDUF
# Big Design Up Front



# SOLID
# S: Принцип единственной ответственности / Single Responsibility Principle
# O: Принцип открытости/закрытости / Open‐Closed Principle
# L: Принцип подстановки Барбары Лисков / Liskov Substitution Principle
# I: Принцип разделения интерфейсов / Interface Segregation Principle
# D: Принцип инверсии зависимостей / Dependency Inversion Principle


