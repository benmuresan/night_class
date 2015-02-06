__author__ = 'Beni'


# Why is it that my function is not receiving the input from the "while True statemnt?

def hello_name(name):
    print "Hello {}!".format(name)


while True:

    name = raw_input("What is your name? If you would like to quit press 'q' ")

    if name == "q":
        break
    else:
        hello_name(name)