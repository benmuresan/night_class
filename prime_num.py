__author__ = 'Beni'


# print("I can find every prime number between 1 and whatever your number is.")
#
# number = int(input("What is your number? "))
#
# num_to_check = range(1, number + 1)
#
# for i in num_to_check:
#
#     check_against = range(2, i)
#     for j in check_against:
#         if i % j == 0 or i == 1:
#             print("{} is not a prime number!".format(j))
#             break
#     else:
#         print("{} is a prime number!".format(i))
#



number = int(input('Enter:'))

for num in range(1, number + 1):

    for i in range(2, num):
        if num % i == 0 or num == 1:
            print num
            break

    else:
        print num, "is a prime number"

number = int(input("Enter your number: "))

# # for num in