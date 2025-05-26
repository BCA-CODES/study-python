def func(num):
    def func2(a):
        return a ** num
    return func2

x = func(2)


print(x(3))
