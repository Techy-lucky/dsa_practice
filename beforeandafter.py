# # before
# def f(n):
#     if n==0:
#         return
#     print(n)
#     f(n-1)

# f(3)

# # after
# def f(n):
#     if n==0:
#         return
#     f(n-1)
#     print(n)
# f(3)

def f0():
    return

def f1():
    print(1)
    f0()

def f2():
    print(2)
    f1()

def f3():
    print(3)
    f2()

f3()     # you call it ONE time