import os

clear = lambda: os.system('clear')

print"*"*75

pos_score = range(1, 11)
clear()
print"*"*75
print(" ")
print("The lowest possible score is {}, and the highest possible score is {}.".format(pos_score[0], pos_score[9]))
print(" ")
print"*"*75
print(" ")
for i in pos_score:
    if i == 1:
        print("A judge can give a gymnast {} point.".format(i))
    else:
        print("A judge can give a gymnast {} points.".format(i))
