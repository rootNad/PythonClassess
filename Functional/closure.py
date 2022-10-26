# def say_name(name):
#     def say_goodbye():
#         print(f"Don't say me goodbye, {name}!")
#     say_goodbye()

# say_name("Bob")


import string


def say_name(name):
    def say_goodbye():
        print(f"Don't say me goodbye, {name}!")

    return say_goodbye

f1 = say_name("Bob")
f2 = say_name("Alex")
f1()
f2()





def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step


c1 = counter(10)
c2 = counter(0)
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())



def add(num1=1):
    def do_add(num2):
        return num1 + num2
    return do_add

a1 = add(5)
print(a1(1))
print(a1(2))
print(a1(3))
print(a1(4))
print(a1(5))

a2 = add(10)
print(a2(10))
print(a2(20))
print(a2(30))
print(a2(40))
print(a2(50))
