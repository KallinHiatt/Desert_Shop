from dessert import DesertItem, Candy, Cookie, IceCream, Sundae
def test_candy():
    candy = Candy("Tootsie Rolls", 15.3, 15.00)
    name = candy.get_name()
    assert name == "Tootsie Rolls"
    weight = candy.get_weight()
    assert weight == 15.3
    price = candy.get_price_per_pound()
    assert price == 15.00
    
#-------------------------------------------------    
def test_cookie():
    cookie = Cookie("Chocolate Chip", 2, 2.00 )
    name = cookie.get_name()
    assert name == "Chocolate Chip"
    quantity = cookie.get_quantity()
    assert quantity == 2
    price = cookie.get_price()
    assert price == 2.00
    
#-------------------------------------------------    
def test_icecream():
    icecream = IceCream("Vanilla", 3, 2.00)
    name = icecream.get_name()
    assert name == "Vanilla"
    counts = icecream.get_scoop_counts()
    assert counts == 3
    price = icecream.get_price()
    assert price == 2.00
    
#-------------------------------------------------  
def test_sundae():
    sundae = Sundae("Chocolate Sundae", 3, 2.00, "Chocolate Syrup", 0.50)
    name = sundae.get_name()
    assert name == "Chocolate Sundae"
    counts = sundae.get_scoop_counts()
    assert counts == 3
    price = sundae.get_price()
    assert price == 2.00
    flavor = sundae.get_topping_name()
    assert flavor == "Chocolate Syrup"
    topping_price = sundae.get_topping_price()
    assert topping_price == 0.50
    
    
print(test_candy())
print(test_cookie())
print(test_icecream())
print(test_sundae())
