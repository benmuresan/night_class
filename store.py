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
        self.cart = []

    def buy(self, item):
        self.balance = self.balance - item.get("price")
        self.cart.append(item)
        self.balance = self.balance - item.get("price")
        self.pay = Store.money + item.get("price")

bens_store = Store()

cust1 = Customer()

cust1.buy("bread")

if "Bread" in bens_store.inventory:
    item = bens_store.inventory.get("Bread")


