def car (want_a_car, color, doors, cost):
	if want_a_car.lower() == "yes" or want_a_car.lower() == "y":
		print "Great!"
		print "You want a %s car.  We can do that!" % color
		print "you want %s doors.  I guess that's alright." % doors
		if int(cost) < 5000:
				print "You are way too cheap! Bye"
		else:
			print "Sold!"
	else:
		print "Okay fine, No car for you!!."

want_a_car.lower() = raw_input ("Do you want a car?  ")
color = raw_input ("What color car would you like?  ")
doors = raw_input ("How many doors do you want?:  ")
cost = raw_input ("How much do you want to pay?  ")

