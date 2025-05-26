coffee_size = input("Order your coffee size(small, medium, large) :").lower()
extra_shot = input("Would you like to order with extra shot(True, False)? :").lower()

if extra_shot == "true":
    print(coffee_size + " coffee with a Extra shot of espresso")
else:
    print(coffee_size + " coffee")
