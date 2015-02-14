__author__ = 'Beni'

def adding(x, y):
    return x + y


x = int(input("What is your first number? "))
y = int(input("What is your second number? "))

print "{} + {} = {}".format(x, y, adding(x, y))

