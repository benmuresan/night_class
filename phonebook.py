__author__ = 'Beni'

phonebook = {
    "Nathan":   {"name": "Nathan", "phone": "1231231234"},
    "Ken":      {"name": "Ken", "phone": "4353453456"}
}


def add():
    name = raw_input("What is the new name to enter? ").lower()
    phone = raw_input("What is the new phone number to enter? ")

    phonebook[name] = {"name": name, "phone": phone}
    print name.upper() + " has been added!"


def search():
    name_2 = raw_input("What is the name you would like to search for? ")
    if name_2 in phonebook:
        print phonebook[name_2]
    else:
        print " "
        print " "
        print "That name is not in the phonebook."


def remove():
    to_pop = raw_input("What name would you like to remove? ")
    if to_pop in phonebook:
        phonebook.pop(to_pop)
        print to_pop + " has been removed!"
    else:
        print "That name is not in the phonebook."


def edit():
    change = raw_input("Who's phone number would you like to edit? ").lower()
    new_number = raw_input("What is the new phone number for " + change + " ?")
    phonebook[change]["phone"] = new_number
    print change + "'s number has been updated."


print "-"*75
print " "*75
print "Welcome to the phone book app!"


while True:
    print " "
    print "-"*75
    print " "
    print "Please choose an option."
    print " "
    print "ENTER 1  To add a new person to the phonebook."
    print "ENTER 2  To search the phonebook."
    print 'ENTER 3  To remove a name.'
    print "ENTER 4  To edit an entry."
    print "ENTER 5  To exit."
    print " "
    print "-"*75
    print " "*75

    try:
        prompt = input("> ")
        if prompt == 1:
            add()

        if prompt == 2:
            search()

        if prompt == 3:
            remove()

        if prompt == 4:
            edit()

        if prompt == 5:
            print "Exit.  Goodbye."
            break
    except:
            print "That option is not available."