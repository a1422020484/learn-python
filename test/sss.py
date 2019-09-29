print('Helloworld')


def person(age):
    print(age)


print(32)


# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum;


F = lazy_sum(1, 4, 5, 6)

print(F())


# 闭包

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())

# 匿名函数

f1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6]))
print(f1)


# 装饰器
