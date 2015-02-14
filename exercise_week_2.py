__author__ = 'Beni'

name_list = []
times_greeted = 0


def greeting():
    name = raw_input("What is your name? ")
    name_list.append(name)
    print("Hello, {}".format(name))
    print("{}, I noticed that your working hard today.".format(name))
    print("Work a little less tomorrow {}".format(name))
    print("There are {} people in your list, they are:".format(len(name_list)))
    for i in name_list:
        print i


while True:
    if times_greeted <= 2:
        greeting()
        times_greeted = times_greeted + 1
    else:
        break