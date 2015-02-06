__author__ = 'Beni'

import random

random_num = random.randint(1, 25)
times_guessed = 0

while True:
    if times_guessed == 5:
        print "All is lost, no more guesses!"
        break
    else:
        times_guessed = times_guessed + 1


def protocol(guessed_num):
    if guessed_num == random_num:
        print("You goit it!!")
        break
    elif:
        if guessed_num < random_num:
            print "Our number is less than that."
            times_guessed = times_guessed + 1
    else:
        if (guessed_num) > (random_num):
            print "Our number is greater than that."
            times_guessed = times_guessed + 1






print "I'm thinking of a number between 1 and 25."
guessed_num = int(input("You get 5 trys to figure it out.  Whats your guess? "))
protocol(guessed_num)
