__author__ = 'Beni'

# ##
# VARIABLES AND DATA TYPES
###

# Variable: A named reference to a value
quantity = 144

# Data Type: A Specific kind of variable (e.g. Integer, String, List)

# Number: numbers come in two flavors
# Integer: whole numbers (e.g. 1,2,3)
i = 12
# Float: A floating-point/decimal number can hold fractional values (e.g. 1.0, 0.25 13.79)
f = 33.33
half = 1.0 / 2.0

# String: An ordered sequence of characters
student_name = "Alice Jones"

# List: A list is an ordered collection of values that can be referenced by position in the list [0,1,2,3,...]
# 0 is the index of the first item, 1 is the second item 2 is the third item etc
# -1 is the last item -2 is the second to the last item
people = ["Bob", "Carol", "Ted", "Alice"]
first_person = people[0]
last_person = people[-1]

quarterly_sales_for_year = [100, 75, 50, 200]
q3 = quarterly_sales_for_year[2]

#Dictionary: a dictionary is an unordered collection of values that can be accessed by a name known as a key like a phone book or library
phone_book = {"Bob": "555-555-2222", "Carol": "555-555-3333", "Ted": "555-555-4444", "Alice": "555-555-1111"}
alice_number = phone_book["Alice"]

#Boolean: A Boolean is a binary logical value. e.g. True or False
is_a_student = True
is_cheating = False


###
# EXPRESSIONS AND OPERATORS
###

sum = 2 + 2
product = 3 * 4
fraction = 1 / 2
modulus_remainder = 5 % 4

#Boolean Expressions
is_greater = 7 > 9
is_equal = (9 == (4 + 5))

###
# CONTROL FLOW
###

# CONDITIONALS
# if, elif, else
state = "unknown"
if state == "good":
    destination = "heaven"
elif state == "bad":
    destination = "hell"
else:
    destination = "purgatory"

# LOOPS
# While
# For
alive = False
while alive:
    if can_dance:
        dance()
    else:
        die()

for person in ["Bob", "Carol", "Ted", "Alice"]:
    print person

###
# DEFINING FUNCTIONS
###

#built in functions
print len("word, again")
print len(str(3 * 4))

## Functions are a sequence of code instructions you can call by name to avoid copy paste modify.
# like a useful formula

def celcius(farenheit):
    output = ((farenheit - 32) * 5) / 9
    return output


print "100 -> " + str(celcius(100))

###
# Classes and Modules
###
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Group(list):
    def show(self):
        for person in self:
            print person.first_name + " " + person.last_name

g = Group()

p = Person("Kevin", "Long")
print p.first_name

g.append(p)

g.append(Person("Ashley", "Ford"))

k = g[0]
print k.first_name

g.show()