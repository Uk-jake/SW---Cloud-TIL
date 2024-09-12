import datetime
import functools

def deco(func):
    def inner():
        print("running inner()")
        func()
        print("finished running inner()")
    return inner

@deco
def target():
    print("running target()")

#target()

def logRunTiem(func):
    def inner(*args):
        print("running inner()")
        start = datetime.datetime.now()
        result = func(*args)
        end = datetime.datetime.now()
        print("finished running inner()")
        print("running time: ", end - start)
        name = func.__name__
        return result
    return inner

@functools.lru_cache()
@logRunTiem
def RecursiveFibo(n):
    if n < 2:
        return n
    else:
        return RecursiveFibo(n-1) + RecursiveFibo(n-2)

@logRunTiem
def IterativeFibo(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

print(IterativeFibo(40))
print(RecursiveFibo(40))