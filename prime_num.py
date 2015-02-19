__author__ = 'Beni'




# print("I can find every prime number between 1 and whatever your number is.")
# num_select = int(input("What is your number? "))
#
# num_to_check = range(2, num_select + 1)
#
# for i in num_to_check:
#     for j in i:
#         if num_select % j == 1 or j == 1:
#             break
#     else:
#         print("{} is a prime number!".format(num_to_check))
#
#



number = int(input('Enter:'))

for num in range(1, number + 1):

    for i in range(2, num):
        if num % i == 0 or num == 1:
            # print num
            break

    else:
        print num, "is a prime number"