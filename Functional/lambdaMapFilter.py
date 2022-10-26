# Global keyword
# c = 1

# def add1():
#     print(c)

# # def add2():
# #     c = c + 2
# #     print(c)

# def add3():
#     global c
#     c = c + 2
#     print(c)

# add1()
# # add2()
# add3()

"""
    We can access a global variable
    inside a function, but we can't change it
    in the local scope of function
"""

# Lambda functions

def d_foo(x):
    return x * x

# lambda arg1, arg2, ..., argN: return expression
l_foo = lambda x: x*x

print(d_foo(2))
print(l_foo(2))


# If statement in lambda functions
# lambda arg1, ..., argN: retIfTrueValue if expression else retIfFalseVal

l_foo = lambda x: "even" if x % 2 == 0 else "odd"
print(l_foo(11))


# Map function
# map(function, *iterables)

# Example

# def foo(lst):
#     for i in range(len(lst)):
#         lst[i] = int(lst[i])
#     return lst


# int_list = foo(str_list)
# print(int_list)

str_list = ["1", "2", "3", "4", "5"]
int_list = list(map(int, str_list))
print(str_list)
print(int_list)
# map does not change the object itself


# def add(x, y):
#     return x * y

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# list3 = []
# Iterative
# for i in range(len(list1)):
#     list3.append(add(list1[i], list2[i]))

# print(list3)

# With map and def function

# def add(x, y):
#     return x * y

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# list3 = []

# list3 = list(map(add, list1, list2))
# print(list3)

# With map and lambda function
# list3 = list(map(lambda x, y: x * y, list1, list2))
# print(list3)


# Filter

# def foo(lst):
#     odd_lst = []
#     for i in lst:
#         if i % 2 != 0:
#             odd_lst.append(i)
#     return odd_lst

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = foo(list1)
# print(list2)

# filter(func, iterable)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def foo(num):
#     return num % 2 == 1

# list2 = list(filter(foo, list1))
# print(list2)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list2 = list(filter(lambda x: x % 2 == 1, list1))
# print(list2)


# Reduce

# Iterative
# def foo(lst):
#     total = 0
#     for i in lst:
#         total += i
#     return total

# list1 = [75, 65, 80, 95, 50]
# sum = foo(list1)
# print(sum)


# Reduce
from functools import reduce
# reduce(funct, list) func must get 2 args!

# def sum(a, b):
#     print(f"a={a}, b={b}, {a} + {b} = {a + b}")
#     return a + b

# list1 = [75, 65, 80, 95, 50]
# print(list1)
# total = reduce(sum, list1)
# print(total)


# With lambda
# list1 = [75, 65, 80, 95, 50]
# total = reduce(lambda a, b: a + b, list1)
# print(total)

