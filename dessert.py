class DesertItem:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name
class Candy(DesertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    def get_weight(self):
        return self.candy_weight
    def get_price_per_pound(self):
        return self.price_per_pound
#------------------------------------------------
class Cookie(DesertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen
    def get_quantity(self):
        return self.quantity
    def get_price(self):
        return self.price_per_dozen
#-------------------------------------------------
class IceCream(DesertItem):
    def __init__(self, name, scoop_counts, price_per_scoop):
        super().__init__(name)
        self.scoop_counts = scoop_counts
        self.price_per_scoop = price_per_scoop
    def get_scoop_counts(self):
        return self.scoop_counts
    def get_price(self):
        return self.price_per_scoop
#-------------------------------------------------
class Sundae(IceCream):
    def __init__(self, name, scoop_counts, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_counts, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def get_topping_name(self):
        return self.topping_name
    def get_topping_price(self):
        return self.topping_price

candy_corn = Candy("Candy Corn", 1.5, .25)
gummy_bear = Candy("Gummy Bears", .25, .35)
chocolate_chip = Cookie("Chocolate Chip", 6, 3.99)
icecream = IceCream("Pistachio", 2, .79)
vanilla = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
oatmeal_rasin = Cookie("Oatmeal Raisin", 2, 3.45)


class Order:
    stuff = [candy_corn.name, gummy_bear.name, chocolate_chip.name, icecream.name, vanilla.name, oatmeal_rasin.name]
    print("\n".join(stuff))
    print(f"Total number of items in order: {len(stuff)}")

"""
stuff = []
while True:
    order = input("What would you like to order? (Type: 'cookie', 'candy', 'icecream', or 'sundae')\n")
    if order == "cookie":
        print(f"We have {chocolate_chip.name} and {oatmeal_rasin.name} cookies.\n")
        cookie = input("What cookie would you like? (Type: 'oatmeal' or 'chocolate' or 'nevermind')\n")
        if cookie == 'oatmeal':
            print("Here's your oatmeal cookie.")
            stuff.append(oatmeal_rasin.name)
        if cookie == 'chocolate':
            print("Here's your chocolate chip cookie.")
            stuff.append(chocolate_chip.name)
        if cookie == "nevermind":
            continue
    if order == "candy":
        print(f"We have {candy_corn.name} and {gummy_bear.name}s.")
        candy = input("What candy would you like? (Type: 'corn' or 'bear' or 'nevermind')\n")
        if candy == "corn":
            print("Here's your candy corn.")
            stuff.append(candy_corn.name)
        if candy == 

"""