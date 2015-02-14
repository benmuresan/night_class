__author__ = 'Beni'

import os

clear = lambda: os.system('clear')
clear()

print "*"*75
print("Ben Muresan's first quiz")
print "*"*75
print(" ")

print("Hello World")

print(" ")
print "*"*75
print(" ")

fruit = ["Apples", "Oranges", "Bananas"]

print(fruit)

print(" ")
print "*"*75
print(" ")

fruit[1] = "Grapes"

for i in fruit:
    print i


print(" ")
print "*"*75
print(" ")


people = {

    "Bob": {"name": "Bobb", "age": "22"},
    "Carol": {"name": "Caroline", "age": "47"},
    "Justin": {"name": "Jake", "age": "14"}
}

for index, person in people.items():
    print index, person["name"], person["age"]

for person in people:
    for field in person:
        print field

# for person in people:
#     print person[0], person[1]

# def add(a, b):
#     print a + b
#
#
# add(5, 5)
# add(10, 15)
# add(3, 6)
#
# print(" ")
# print "*"*75
# print(" ")
#
# #
# # def plus_5():
# #     user_num = int(input("What is your #?  We will add 5 to it until we reach 1000. "))
# #     return user_num
#
# # total = int(input("What is your #?  We will add 5 to it until we reach 1000. "))
#
#
# def plus_5():
#     total = int(input("What is your #?  We will add 5 to it until we reach 1000. "))
#     while True:
#         if total <= 995:
#             print total + 5
#             total = total + 5
#         else:
#             print("All done your total is now {}".format(total))
#             break
#
# plus_5()
#
# print(" ")
# print "*"*75
# print(" ")
#
# #  No idea how to do #10.
# #  print("I have no idea how to do the " + "Fizzbuzz"+" exercise")
#
#
# def fizbuzz():
#     x = range(1, 101)
#     for i in x:
#         if i % 3 == 0 and i % 5 == 0:
#             print "Fizzbuzz"
#         elif i % 3 == 0:
#             print "Fizz"
#         elif i % 5 == 0:
#             print "Buzz"
#         else:
#             print i
#
# fizbuzz()
#
#
# # def modulus():
# #     x = range(1, 101)
# #     for i in x:
# #         if i % 3 == 0 and i % 5 == 0:
# #             print("FizzBuzz!")
# #         elif i % 3 == 0:
# #             print("Fizz")
# #         elif i % 5 == 0:
# #             print("Buzz")
# #         else:
# #             print i
#
# print(" ")
# print "*"*75
# print(" ")
#
#
# class Customer():
#     def __init__(self, name, age):
#         self.cust_name = name
#         self.cust_age = age
#         self.cust_location = "Washington"
#         self.cust_cscore = 718
#
#
# customer1 = Customer("Jessie", "30")
#
# print("The customers name is {}.".format(customer1.cust_name))
# print("The customers location is {}.".format(customer1.cust_location))
# print("The customers credit score is {}.".format(customer1.cust_cscore))
#
# customer1.cust_cscore = 800
#
# print(" ")
# print("*" * 75)
# print(" ")
#
# print("{}'s new credit score is now {}.".format(customer1.cust_name, customer1.cust_cscore))
#
# print(" ")
# print "*"*75
# print(" ")