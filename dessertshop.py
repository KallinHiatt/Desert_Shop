
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
from receipt import make_receipt

class Order():
    def __init__(self):
        self.order = []
    def add(self, dessertitem):
        self.order.append(dessertitem)
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        cost = 0.0
        for item in self.order:
            cost += item.calculate_cost()
        return cost
    def order_tax(self):
        tax = 0.0
        for item in self.order:
            tax += item.calculate_cost() * (item.tax_percent/100)
        return tax

class DesertShop():
    def user_prompt_candy(self):
        print("Type in the name of the candy (str), the weight in pounds (flt), and the price per pound (flt)")
        while True:
            candy_name = input("Candy name: ")
            if isinstance(candy_name, str):
                break
            else:
                print("That's not a string...")
                continue
        while True:
            weight = float(input("Candy weight: "))
            if isinstance(weight, float):
                break
            else:
                print("That's not a float...")
                continue
        while True:
            price = float(input("Price per pound: "))
            if isinstance(price, float):
                break
            else:
                print("That's not a float...")
                continue
        candy1 = Candy(candy_name, weight, price)
        return candy1

    def user_prompt_cookie(self):
        print("Type in the name of the cookie (str), the amount of cookies (int), and the price per dozen (flt)")
        while True:
            cookie_name = input("Cookie name: ")
            if isinstance(cookie_name, str):
                break
            else:
                print("That's not a string...")
                continue
        while True:
            amount = int(input("Cookie amount: "))
            if isinstance(amount, int):
                break
            else:
                print("That's not a integer...")
                continue
        while True:
            price12 = float(input("Price per dozen: "))
            if isinstance(price12, float):
                break
            else:
                print("That's not a float...")
                continue
        cookie1 = Cookie(cookie_name, amount, price12)
        return cookie1

    def user_prompt_icecream(self):
        print("Type in the name of the icecream (str), the amount of scoops (int), and the price per scoop (flt)")
        while True:
            icecream_name = input("Icecream name: ")
            if isinstance(icecream_name, str):
                break
            else:
                print("That's not a string...")
                continue
        while True:
            scooby_number = int(input("How many scoops: "))
            if isinstance(scooby_number, int):
                break
            else:
                print("That's not a integer...")
                continue
        while True:
            scooby_price = float(input("Price per scoop: "))
            if isinstance(scooby_price, float):
                break
            else:
                print("That's not a float...")
                continue
        icecream1 = IceCream(icecream_name, scooby_number, scooby_price)
        return icecream1

    def user_prompt_sundae(self):
        print("Type in the name of the ice cream(str), the scoop count(int), the price per scoop(float), topping name(str), and topping price(float).")
        while True:
            sundae_name = input("Ice cream name: ")
            if isinstance(sundae_name, str):
                break
            else:
                print("That's not a string. Type in a string.")
                continue
        while True:        
            scoop_num = int(input("Amount of scoops: "))
            if isinstance(scoop_num, int):
                break
            else:
                print("That's not an integer. Type in an integer.")
                continue
        while True:
            scoop_price = float(input("Price per scoop: "))
            if isinstance(scoop_price, float):
                break
            else:
                print("That's not a float. Type in a float.")
                continue
        while True:
            topping_name = input("Price per scoop: ")
            if isinstance(topping_name, str):
                break
            else:
                print("That's not a string. Type in a string.")
                continue
        while True:
            topping_price = float(input("Price per scoop: "))
            if isinstance(topping_price, float):
                break
            else:
                print("That's not a float. Type in a float.")
                continue
        sundae1 = Sundae(sundae_name, scoop_num, scoop_price, topping_name, topping_price)
        return sundae1


def main(Order):
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    print("Candy Corn")
    order1.add(Candy("Gummy Bears", .25, .35))
    print("Gummy Bears")
    order1.add(Cookie("Chocolate Chip", 6, 3.99))
    print("Chocolate Chip")
    order1.add(IceCream("Pistachio", 2, .79))
    print("Pistachio")
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    print("Vanilla")
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))
    print("Oatmeal Raisin")
    print(f"Total number of items in order: {order1.__len__()}")
    data = []
    for item in order1.order:
        if isinstance(item, Candy):
            data.append([item.name, item.candy_weight, item.price_per_pound])
        elif isinstance(item, Cookie):
            data.append([item.name, item.cookie_quantity, item.price_per_dozen])
        elif isinstance(item, IceCream):
            data.append([item.name, item.scoop_count, item.price_per_scoop])
        elif isinstance(item, Sundae):
            data.append([item.name, item.scoop_count, item.price_per_scoop, item.topping_name, item.topping_price])
    data.append(["Order Subtotals", "$"+str(round(order1.order_cost(), 2)), "$" + str(round(order1.order_tax(), 2))])
    data.append(["Total", "", "$" + str(round(order1.order_cost() + order1.order_tax(), 2))])
    data.append(["Total items in the order", "", str(order1.__len__())])
    import receipt
    receipt.make_receipt(data, "receipt.pdf")
    print(data)


main(Order)

