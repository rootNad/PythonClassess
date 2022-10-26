# # Generator
# def foo(arg):
#     yield arg

# v = foo(10)
# # print(v)
# # print(next(v))
# # print(next(v))


# def fruits():
#     yield "Mango"
#     yield "Jackfruit"
#     yield "Banana"
#     yield "Guava"

# gf = fruits()
# # print(gf)
# # print(next(gf))
# # print(next(gf))
# # print(next(gf))
# # print(next(gf))

# # for fruit in gf:
# #     print(fruit)
# # # or
# # for fruit in fruits():
# #     print(fruit)

# # def timesTable(number):
# #     for i in range(1, 11):
# #         yield i * number
# #         i += 1

# # gettimes_1 = timesTable(10)

# # print(next(gettimes_1))
# # print(next(gettimes_1))
# # print(next(gettimes_1))
# # print(next(gettimes_1))
# # print(next(gettimes_1))
# # print(next(gettimes_1))

# # print()

# # for i in gettimes_1:
# #     print(i)


# # Iterator
# lst = [1, 2, 3, 4, 5]
# iter_lst = iter(lst)
# output = next(iter_lst)

# print(iter_lst)
# print(type(iter_lst))
# print(next(iter_lst))
# print(output)



# # Fibonacci numbers with generators
# def fib(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# for i in fib(10):
#     print(i)



def ng(n):
    if n < 20:
        number = 0
        while number < n:
            yield number
            number += 1
    else:
        return


for i in ng(19):
    print(i)


gen = ng(10)
counter = 0
while counter < 10:
    print(next(gen))
    counter += 1