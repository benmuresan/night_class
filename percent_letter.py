__author__ = 'Beni'

user_string = input("Whats your word? ")
user_num = input("Whats you number? ")

try:
    our_num = int(user_num)
except:
    our_num = float(user_num)

if not "." in user_num:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    print(user_string[ratio])