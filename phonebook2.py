__author__ = 'Beni'

phonebook = {

    'Nathan': {"name": "Nathan", "phone": "1231231234"},
    'Ken': {"name": "Ken", "phone": "2342342345"}
}

def add():
    add_name = raw_input("What name should we add to the phonebook? ")
    new_number = raw_input("What is " + add_name + "'s phone number? ")
    phonebook[add_name] = {"name": add_name, "phone": new_number}
    print " "
    print " "
    print add_name + " Has been added to the phone book."
    print add_name + "'s phone number is " + new_number + "."
    print " "
    print " "


def remove():
    to_remove = raw_input("What name should we remove? ")
    try:
        phonebook.pop(to_remove)
        print " "
        print to_remove + " Has been removed from the phonebook."
    except:
        print " "
        print to_remove + " is not available to be removed."

def edit():
    changed_num = raw_input("Who's number would you like to edit? ")
    print ' '
    new_num = raw_input("What is " + changed_num + "\'s new number? ")
    phonebook[changed_num]["phone"] = new_num
    print "{} 's phone number has been updated to {}.".format(changed_num, new_num)

def search():
    name_to_find = raw_input("What name should we search for? ")
    if name_to_find in phonebook:
        print name_to_find + " Is in the phonebook, here is the info."
        print phonebook[name_to_find: "name"]
        print phonebook[name_to_find: "phone"]


print "-"*75
print " "
print "Welcome to our fancy Phonebook!"
print " "
print " "

while True:

    print "-"*75
    print " "
    print "Make a selection."
    print " "
    print "-"*75
    print " "

    print "ENTER 1 to add a name to the Phonebook. "
    print "ENTER 2 to remove an entry. "
    print "ENTER 3 to edit an entry. "
    print "ENTER 4 to search for an entry. "
    print "ENTER 5 to exit program. "
    print " "

    try:

        user_input = int(raw_input("?> "))

        if user_input == 1:
            add()

        if user_input == 2:
            remove()

        if user_input == 3:
            edit()

        if user_input == 4:
            search()

        if user_input ==5:
            print " Exit, Goodbye!"
            break

    except:
         print "That is not an option."