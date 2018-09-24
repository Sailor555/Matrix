from functools import wraps


def wrap(func):
    #@wraps(func)
    def callf(*args, **kwargs):
        return func(*args, **kwargs)
    return callf

@wrap
def factorial(n):
    #"""阶乘函数：n!"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial.at = "属性"
factorial.at2 = [1,2,3]


print(factorial(3))
print(factorial.__doc__)
print(factorial.at)
print(factorial.at2)