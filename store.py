__author__ = 'Beni'


class Store(object):
    def __init__(self):
        self.inventory = {
            "Bread":   {"price": 2, "quantity": 5},
            "Milk":    {"price": 1, "quantity": 10}
        }
        self.customers = []
        self.money = 0


class Customer(object):
    def __init__(self):
        self.name = ""
        self.balance = 0
        self.cart = {}

    def buy(self, store, item, quantity):
        self.balance -= (store.inventory[item]["price"] * quantity)
        self.cart[item] = quantity
        store.money += (store.inventory[item]["price"] * quantity)
        store.inventory[item]["quantity"] -= quantity



kens_store = Store()
nathans_store = Store()

cust1 = Customer()
cust2 = Customer()

cust1.buy(kens_store, "Bread", 2)
cust2.buy(nathans_store, "Milk", 2)

print str(kens_store.money) + "\n"
print str(kens_store.inventory) + "\n"
print str(nathans_store.money) + "\n"
print str(nathans_store.inventory) + "\n"
print(cust1.cart)
print(cust1.balance)

# if "Bread" in bens_store.inventory:
#     item = bens_store.inventory.get("Bread")


