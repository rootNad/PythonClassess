# def call_with_five(func):
#     return func(5)

# def add_one(x):
#     return x + 1

# # print(call_with_five(add_one))
# # print(call_with_five(add_one))
# # print(call_with_five(add_one))
# # print(call_with_five(add_one))
# # print(call_with_five(add_one))


def power_generator(base):
    return lambda x: pow(x, base)

# or
# def power_generator_func(base):
#     def power(x):
#         return pow(x, base)
#     return power

square = power_generator(2)
print(square(2))
print(square(3))
print(square(4))
print(square(5))

cube = power_generator(3)
print(cube(2))
print(cube(3))
print(cube(4))
print(cube(5))




# def add(x):
#     def inner(y):
#         def inner2(z):
#             return x + y + z
#         return inner2
#     return inner

# a = add(1)(2)(3)
# print(a)


# function currying
# not curried function
def add1(n1, n2):
    return n1 + n2
print(add1(1, 2))

# curried function

def add2(n1):
    def fn(n2):
        return n1 + n2
    return fn
print(add2(1)(2))
f1 = add2(5)
print(f1(5))

# With lambda
# not curried function
f1 = lambda x, y: x + y
print(f1(1, 2))
# curried function
f2 = lambda x: lambda y: x + y
print(f2(1)(2))
