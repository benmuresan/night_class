# print "Hello World"

# print 1234 * 1234

# a = 5

# print a

# a = 6
# print a 

# print type(5.4)

print "Welcome to the wild world of random questions!"
print "Let us begin"

name = raw_input ("What is your name?  ")
age = input ("How old are you?: ")
hair = raw_input ("What color is your hair? ")
age_add = input ("How many years would you like me to add to your life?")

print "Your name is " + name + "."
print "Your name is %s. You are %s years old.  And your hair is %s" % (name, age, hair)


print "In %s years you will be %s."  % (age_add, (age + age_add))

if hair == "brown":
	print "Because your hair is Brown, you'll lose it soon."
	
elif hair == "red"
	print "Your hair is red!"
else:
	print "Because your hair is not Brown but %s you'll have it forever." % (hair)