# 装饰器

# 1.函数
# 1.1 定义
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    return

# 1.2 调用
func(1, "Hello", [1, 2, 3], (1, 2), {1, 2}, kw1=12, kw2="abc")

# 1.3 作为数据（函数对象）
f = func
def callf(f):
    f(1, "Hello", [1, 2, 3], (1, 2), {1, 2}, kw1=12, kw2="abc")
callf(func)
def outer1():
    return func
outer1()(1, "Hello", [1, 2, 3], (1, 2), {1, 2}, kw1=12, kw2="abc")

# 1.4 闭包（closure）
def outer2(x):
    def inner():
        print(x)
    return inner
closure = outer2(10)
closure()

# 1.5 装饰器（decorate）
def foo():
    print("foo")
# 任务:添加日志功能
# Solution1 : 直接修改原函数代码
# def foo():
#     print("记录日志开始...")
#     print("foo")
#     print("记录日志结束!")
# Solution2 : 装饰器
def outer3(f):
    def inner():
        print("记录日志开始...")
        f()
        print("记录日志结束!")
    return inner
foo = outer3(foo)
foo()
