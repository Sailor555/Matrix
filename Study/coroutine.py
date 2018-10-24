import os
import fnmatch

# 装饰器：执行第一次调用__next__()动作
def coroutine(func):
    def inner(*args, **kwargs):
        f = func(*args, **kwargs)
        f.__next__()
        return f
    return inner

# Generator Demo
def g_find_files(topdir, pattern):
    for path,dirname,filelist in os.walk(topdir):
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                print("Enter: ", os.path.join(path, name))
                yield os.path.join(path, name)


import gzip, bz2
def g_opener(filenames):
    for name in filenames:
        f = open(name, encoding='gb18030', errors='ignore')
        yield f


def g_cat(filelist):
    for f in filelist:
        for line in f:
            yield line


def g_grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

# Generator Usage
# filenames = g_find_files("d:\\testdata", "*")
# fileopened = g_opener(filenames)
# lines = g_cat(fileopened)
# widthlines = g_grep("width", lines)
# for line in widthlines:
#     print(line)

# Coroutine Demo
@coroutine
def c_find_files(target):
    while True:
        topdir, pattern = (yield)
        for path, dirname, filelist in os.walk(topdir):
            for name in filelist:
                if fnmatch.fnmatch(name, pattern):
                    print("Enter: ", os.path.join(path, name))
                    target.send(os.path.join(path, name))


@coroutine
def c_opener(target):
    while True:
        name = (yield )
        f = open(name, encoding='gb18030', errors='ignore')
        target.send(f)


@coroutine
def c_cat(target):
    while True:
        f = (yield )
        for line in f:
            target.send(line)


@coroutine
def c_grep(pattern, target):
    while True:
        line = (yield )
        if pattern in line:
            target.send(line)


@coroutine
def c_printer():
    while True:
        line = (yield )
        print(line)

# Coroutine Usage
finder = c_find_files(c_opener(c_cat(c_grep("width", c_printer()))))
finder.send(("d:\\testdata", "*"))
