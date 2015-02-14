__author__ = 'Beni'


def f(x, func):
    x += 1
    return func(x)


def g(y):
    return y*2

print f(2, g)
