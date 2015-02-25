__author__ = 'Beni'


class Store(object):
    def __init__(self):
        self.inventory = {
            "Bread":   {"price": 2, "quantity": 5},
            "Milk":    {"price": 1, "quantity": 10}
        }
        self.customers = []
        self.money = 0

    def stock(self):
        for index, item in self.inventory.items():
            print index, item["quantity"]

    def names(self):
        for c in self.customers:
            print c.name

    def is_item_available(self, item_name, quantity, ):
        if not item_name in self.inventory:
            return False
        if quantity > self.inventory[item_name]["quantity"]:
            return False
        return True

    def buy(self, customer, item, quantity):
        if self.is_item_available(item, quantity) is True:
            if customer.balance >= (self.inventory[item]["price"] * quantity):
                self.inventory[item]["quantity"] -= quantity
                customer.balance -= (self.inventory[item]["price"] * quantity)
                customer.cart[item] = quantity
                self.money += (self.inventory[item]["price"] * quantity)

                # Adds the customer to the store's customer list.  Need help here to make it specific.
                self.customers.append(customer)
                return ("{} added to {}'s cart.".format(item, customer.name))
            else:
                return ("There are not enough funds available for that!")
        else:
            return ("There is not enough {} in the store to buy {} {}'s.".format(item, quantity, item))

    def print_custs(self):
        for customer in self.customers:
            print("{} has this in his cart: ".format(customer.name))
            customer.pretty_cart()


class Customer(object):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.cart = {}

    def pretty_cart(self):
        for name, qty in self.cart.items():
            print name, qty


kens_store = Store()
# nathans_store = Store()

cust1 = Customer('Ben', 50)
cust2 = Customer('Nathan', 100)

# Next line adds apples to the inventory of a specific store.
kens_store.inventory["Apples"] = {"price": 3, "quantity": 5}


result = kens_store.buy(cust1, "Bread", 1)
print(result)


result = kens_store.buy(cust2, "Apples", 2)
print(result)


print "Kens store has ${}.".format(str(kens_store.money)) + "\n"
print "Kens store has this inventory: " + "\n"

kens_store.stock()

kens_store.print_custs()


#
# print "{} has this in his cart: {}.".format(cust1.name, cust1.cart)
# print "Customer 1 has this much in his wallet ${}.".format(cust1.balance)

# print "{} has this in his cart: {}.".format(cust2.name, cust2.cart)
# print "Customer 2 has this much in his wallet ${}.".format(cust2.balance)
# kens_store.names()
#
# print(len(kens_store.customers))
